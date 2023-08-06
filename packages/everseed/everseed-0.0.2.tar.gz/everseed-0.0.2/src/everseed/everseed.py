#!/usr/bin/env python3 -tt
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    python everseed.py --torrent_input_dir <input_dir> --torrent_output_dir <output_dir> --downloads_dir <downloads_dir>

DESCRIPTION

    An interactive tool used to seed lots of torrents forever

AUTHOR

    Vivek Revankar <vivek@master-hax.com>

"""

__appname__ = "everseed"
__author__  = "Vivek Revankar <vivek@master-hax.com>"
__version__ = "0.0.1"
__license__ = "License"

import sys
from datetime import datetime
import logging.config
import logging
import argparse
import prompt_toolkit
import csv
import os
import glob

from pathlib import Path
from pyrosimple.util import metafile
from pyrosimple.util.ui import HashProgressBar

logger = logging.getLogger(__appname__)
processingLogger = logging.getLogger("processed")

def process_torrent(torrent_details, downloads_dir, output_dir, shouldHashCheck = False, archive_dir = None, overridesMap = None):

    torrent = torrent_details[0]
    torrent_sub_path = torrent_details[1]
    torrent_abs_path = torrent_details[2]

    logger.info("processing torrent " + torrent_sub_path)

    print_torrent_details(torrent_details)

    torrent.clean_meta(including_info=False)

    default_data_path = downloads_dir + "/" + torrent["info"]["name"]
    data_path = ""
    action_taken = ""
    if overridesMap != None and torrent_sub_path in overridesMap:
        action_taken += "override_location"
        overridden_download_location = overridesMap[torrent_sub_path].replace("{}", torrent["info"]["name"])
        if os.path.isabs(overridden_download_location):
            data_path = overridden_download_location
        else:
            data_path = downloads_dir + "/" + overridden_download_location
        logger.info("overriding default data location " + default_data_path + " with " + data_path)
    else:
        action_taken += "datadir"
        data_path = default_data_path
        logger.info("using default data directory " + data_path)
    
    if shouldHashCheck:
        action_taken += "|hashcheck"
        logger.info("hash checking data files...")
        timerPreHashCheck = datetime.now()
        data_ok = hashcheck_torrent(torrent, data_path)
        timerPostHashCheck = datetime.now()
        if not data_ok:
            logger.info("hash check failed in " + str((timerPostHashCheck - timerPreHashCheck).seconds) + " seconds")
            return
        else:
            logger.info("hash check succeeded in " + str((timerPostHashCheck - timerPreHashCheck).seconds) + " seconds")
    else:
        action_taken += "|fastresume"
        logger.info("fast processing data files")
    
    try:
        torrent.add_fast_resume(Path(data_path))
    except OSError as exc:
        logger.warning("error while generating fast resume data " + str(exc))
        return

    # write new torrent to fast_resume_path
    fastresume_path = output_dir + "/" + torrent_sub_path.replace(".torrent","-with-fast-resume.torrent")
    fastresume_sub_dir = os.path.dirname(fastresume_path)
    logger.info("writing fast resume data to" + fastresume_path)
    if not os.path.exists(fastresume_sub_dir):
        logger.info("output directory " + fastresume_sub_dir + " does not exist, attempting to create it recursively")
        try:
            os.makedirs(fastresume_sub_dir)
        except OSError as exc:
            logger.error("could not create output directory " + str(exc))
            return
    try:
        torrent.save(Path(fastresume_path))
    except OSError as exc:
        logger.error("could not save fast resume torrent " + str(exc))
        return

    # move old torrent to archive dir
    if archive_dir == None:
        action_taken += "|in_place"
        logger.info("no archive directory specified, leaving existing torrent in place")
    else:
        action_taken += "|archived"
        archive_path = archive_dir + "/" + torrent_sub_path
        logger.info("moving old torrent to " + archive_path)
        archive_sub_dir = os.path.dirname(archive_path)
        if not os.path.exists(archive_sub_dir):
            logger.info("archive directory " + archive_sub_dir + " does not exist, attempting to create it recursively")
            try:
                os.makedirs(archive_sub_dir)
            except OSError as exc:
                logger.error("could not create archive directory " + str(exc))
                return
        os.rename(torrent_abs_path, archive_path)
    
    # done
    logger.info("torrent processed successfully")
    processingLogger.debug(torrent_sub_path
        + "\t" + data_path
        + "\t" + action_taken
        + "\t" + datetime.now().isoformat()
    )

def hashcheck_torrent(torrent, data_path):
    with HashProgressBar() as pb:
        try:
            return torrent.hash_check(
                Path(data_path),
                progress_callback=pb().progress_callback,
            )
        except OSError as exc:
            logger.warning("error while hash checking data " + str(exc))
            return False
        except KeyboardInterrupt as e: # Ctrl-C
            logger.warning("received keyboard interrupt, cancelled hash check")
            return False

def load_torrent(torrent_file, base_path):
    torrent_sub_path = os.path.relpath(torrent_file, base_path)
    logger.info("loading file " + torrent_sub_path)
    # validate the torrent file metadata
    try:
        torrent = metafile.Metafile.from_file(Path(torrent_file))
    except (OSError, KeyError, bencode.BencodeDecodeError) as exc:
        logger.warning("bad metafile: " + str(exc))
        return None
    else:
        logger.debug("metafile loaded")
        try:
            torrent.check_meta()
        except ValueError as exc:
            logger.warning("metafile failed integrity check " + str(exc))
            return None
        else:
            return (torrent,torrent_sub_path,torrent_file)

def refresh_torrent_data(path):
    logger.info('refreshing torrent list from ' + path)
    if not os.path.exists(path):
        logger.warning("torrent input directory was not found")
        return
    ret = glob.glob(path + '/**/*.torrent')
    logger.info('found ' + str(len(ret)) + ' torrent(s)')
    return ret

def refresh_override_data(path):
    ret = {}
    if path == None:
        logger.info('overrides file not configured')
        return ret
    logger.info('checking for overrides at ' + path)
    if not os.path.exists(path):
        logger.warning("override config file not found")
        return ret
    with open(path, "r") as overrides_file:
        overrides_reader = csv.reader(overrides_file, delimiter='\t')
        for row in overrides_reader:
            if len(row) == 0:
                continue
            elif len(row) != 2 or not row[0].endswith('.torrent'):
                logger.warning("found bad row in overrides file: " + str(row))
                continue
            ret[row[0]] = row[1]
    logger.info("loaded " + str(len(ret)) + " override(s)")
    return ret

def print_torrents(torrent_list, basepath):
    print('listing torrents')
    print('-' * 79)
    for i, elem in enumerate(torrent_list):
        print(str(i) + ' ' + os.path.relpath(elem, basepath))
    print('-' * 79)

def print_overrides(overrides_map):
    print('listing overrides')
    print('=' * 79)
    for torrent,download_dir in overrides_map.items():
        print("* " + torrent + ' -> ' + download_dir)
    print('=' * 79)

def print_torrent_details(torrentTuple):
    print(torrentTuple[1])
    print('~' * 79)
    for line in torrentTuple[0].listing():
        print(line)
    print('~' * 79)

def promptForTorrentChoice(torrent_list):
    if not torrent_list:
        print("no torrents were found. try refreshing?")
        return None
    choice = int(prompt_toolkit.prompt("Which torrent? ", validator = prompt_toolkit.validation.Validator.from_callable(
        lambda x: int(x) >= 0 and int(x) < len(torrent_list),
        error_message='torrent number was not valid',
        move_cursor_to_end=True
    )))
    return torrent_list[choice]

def run_interactive(torrent_input_dir, torrent_output_dir, downloads_dir, archives_dir, overrides_file_path):

    torrent_list = []
    overrides_map = {}

    while True:
        choices = ['help', 'refresh', 'list torrents', 'list overrides', 'info', 'hashcheck', 'process']
        choice = prompt_toolkit.prompt('What do you want to do now? ', completer=prompt_toolkit.completion.WordCompleter(choices))
        choice = choice.strip()
        if choice == 'help':
            print(str(choices))
        elif choice == 'r' or choice == 'refresh':
            torrent_list = refresh_torrent_data(torrent_input_dir)
            overrides_map = refresh_override_data(overrides_file_path)
        elif choice == 'lt' or choice == 'list torrents':
            print_torrents(torrent_list, torrent_input_dir)
        elif choice == 'lo' or choice == 'list overrides':
            print_overrides(overrides_map)
        elif choice == 'i' or choice == 'info':
            print_torrent_details(load_torrent(promptForTorrentChoice(torrent_list), torrent_input_dir))
        elif choice == 'h' or choice == 'hashcheck':
            process_torrent(
                load_torrent(promptForTorrentChoice(torrent_list), torrent_input_dir),
                downloads_dir,
                torrent_output_dir,
                shouldHashCheck=True,
                archive_dir=archives_dir,
                overridesMap=overrides_map,
            )
        elif choice == 'hashcheck all':
            for each_torrent in torrent_list:
                process_torrent(
                    load_torrent(each_torrent, torrent_input_dir),
                    downloads_dir,
                    torrent_output_dir,
                    shouldHashCheck=True,
                    archive_dir=archives_dir,
                    overridesMap=overrides_map
                )
        elif choice.startswith("hashcheck "):
            for subchoice in choice.split(" ")[1].split(","):
                process_torrent(
                    load_torrent(torrent_list[int(subchoice)], torrent_input_dir),
                    downloads_dir,
                    torrent_output_dir,
                    shouldHashCheck=True,
                    archive_dir=archives_dir,
                    overridesMap=overrides_map
                )
        elif choice == 'p' or choice == 'process':
            process_torrent(
                load_torrent(promptForTorrentChoice(torrent_list), torrent_input_dir),
                downloads_dir,
                torrent_output_dir,
                shouldHashCheck=False,
                archive_dir=archives_dir,
                overridesMap=overrides_map
            )
        elif choice == 'process all':
            for each_torrent in torrent_list:
                process_torrent(
                    load_torrent(each_torrent, torrent_input_dir),
                    downloads_dir,
                    torrent_output_dir,
                    shouldHashCheck=False,
                    archive_dir=archives_dir,
                    overridesMap=overrides_map
                )
        elif choice.startswith("process "):
            for subchoice in choice.split(" ")[1].split(","):
                process_torrent(
                    load_torrent(torrent_list[int(subchoice)], torrent_input_dir),
                    downloads_dir,
                    torrent_output_dir,
                    shouldHashCheck=False,
                    archive_dir=archives_dir,
                    overridesMap=overrides_map
                )
        else:
            print('invalid choice')

def setup_logging(result_file_name):
    logConfig = {
        "version": 1,
        "formatters": {
            "default": { 
                "format": "%(asctime)s (%(name)s) [%(levelname)s] %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z"
            },
            "raw": { 
                "format": "%(message)s",
                # "datefmt": "%Y-%m-%dT%H:%M:%S%z"
            },
        },
        "handlers": {
            "console": {
                "formatter": "default",
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            __appname__: {
                "level": "DEBUG",
                "handlers": [
                    "console",
                ],
            },
        }
    }
    if result_file_name != None:
        logConfig["handlers"]["resultfile"] = {
            "formatter": "raw",
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": result_file_name,
        }
        logConfig["loggers"]["processed"] = {
            "level": "DEBUG",
            "handlers": ["resultfile"]
        }

    logging.config.dictConfig(logConfig)

    
def get_arguments():
    parser = argparse.ArgumentParser(
        description = "a tool for seeding lots of torrents forever"
    )

    parser.add_argument('--torrent_input_dir', required = True, help = 'the directory to process torrents from')
    parser.add_argument('--torrent_output_dir', required = True, help = 'the directory to write updated torrents with fastresume data')
    parser.add_argument('--downloads_dir', required = True, help = 'the directory that contains download files')

    parser.add_argument('--overrides_file', required = False, default = None, help = 'path to the tsv file containing overridden download locations')
    parser.add_argument('--torrent_archive_dir', default = None)
    parser.add_argument('--verbose', action='store_true', default=False, help='enable verbose output')
    parser.add_argument('--processed_log_file', default=None, help='path to where processed torrents should be logged')

    return parser.parse_args()

def main():
    try:
        args = get_arguments()
        setup_logging(args.processed_log_file)
        logger.debug(__appname__ + " is running")

        logger.debug("configuration: reading torrents from " + args.torrent_input_dir)
        logger.debug("configuration: writing torrents to " + args.torrent_output_dir)
        logger.debug("configuration: scanning download data in " + args.downloads_dir)
        if args.torrent_archive_dir == None:
            logger.debug("configuration: won't move completed torrents")
        else:
            logger.debug("configuration: moving completed torrents to " + args.torrent_archive_dir)
        if args.overrides_file == None:
            logger.debug("configuration: won't check for download location overrides")
        else:
            logger.debug("configuration: reading download location overrides from " + args.overrides_file)
        if args.processed_log_file == None:
            logger.debug("configuration: won't save processing history")
        else:
            logger.debug("configuration: writing processing history to " + args.processed_log_file)

        run_interactive(
            args.torrent_input_dir,
            args.torrent_output_dir,
            args.downloads_dir,
            args.torrent_archive_dir,
            args.overrides_file
        )

    except KeyboardInterrupt as e: # Ctrl-C
        logger.warning("received keyboard interrupt, exiting everseed")
        raise e

    except SystemExit as e: # sys.exit()
        logger.warning("received system exit")
        raise e

    except Exception as e:
        logger.exception("received exception " + str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()