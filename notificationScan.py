import os
import re
import logging

root_path1 = 'absolute project path'

scan_logger = logging.getLogger('notificationScan')
scan_logger.setLevel(logging.DEBUG)

if not len(scan_logger.handlers):  # 单例,加一次handler即可
    fh = logging.FileHandler('notificationScan' + '.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter("%(levelname)-8s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    scan_logger.addHandler(fh)
    scan_logger.addHandler(ch)

def scan_dir(root_path):
    for root, dirs, files in os.walk(root_path):
        # for d in dirs:
            # print('d:{}'.format(os.path.join(root, d)))  # 目录,集合
        for f in files:
            # print('f:{}'.format(os.path.join(root, f)))  # 文件
            file_path = os.path.join(root, f)
            if (os.path.splitext(file_path)[1]) == '.m' or  (os.path.splitext(file_path)[1]) == '.mm':
                try:
                    scan(file_path)
                except Exception as e:
                    # 目前遇到过的错误，文件编码问题
                    scan_logger.error(e);
                else:
                    pass
                finally:
                    pass

comment_pattern = re.compile('NSNotificationCenter')
add_observer_pattern = re.compile('addObserver')
remove_observer_pattern = re.compile('removeObserver')

def scan(path):
    with open(path, 'r') as f:
        i = 0
        file_name = os.path.basename(path)
        scan_logger.info('scan:{}'.format(path))
        has_add_observer = False
        has_remove_observer = False
        has_notification = False
        for line in f.readlines():
            i += 1
            result = re.search(comment_pattern, line)
            if result:
                has_notification = True
                assert isinstance(line, object)
                line = line.strip()
                scan_logger.info('{:20} {:03}:    {:}'.format(file_name, i, line))
                if re.search(add_observer_pattern, line):
                    scan_logger.info('notification add observer')
                    has_add_observer = True
                if re.search(remove_observer_pattern, line):
                    scan_logger.info('notification removed observer')
                    has_remove_observer = True
        scan_logger.info('scan:{} end'.format(file_name))
        if has_notification:
            if (has_add_observer != has_add_observer):
                scan_logger.warning('warning NSNotificationCenter has add:{} NSNotificationCenter has remove:{}'.format(has_add_observer, has_remove_observer))
            else:
                scan_logger.info('FYI: NSNotificationCenter has add:{} NSNotificationCenter has remove:{}'.format(has_add_observer, has_remove_observer))


scan_dir(root_path1)
