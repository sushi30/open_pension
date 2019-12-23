from . import process_excel


def handler(event, context):
    return process_excel.main(event["path"])
