def content_to_file(file_path, content):
    file = open(file_path, "wb")
    file.write(content)
    file.close()
