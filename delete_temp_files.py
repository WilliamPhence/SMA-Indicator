import os

def delete_temp_files(temp_data):

    for filename in os.listdir(temp_data):
        file_path = os.path.join(temp_data, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

temp_data = "C:\Python Projects\SMA Indicator\DATA"
delete_temp_files(temp_data)