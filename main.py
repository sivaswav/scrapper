import download_xtract;

#if __name__ == "__main__":
ep_obj = download_xtract.download_xtract('https://catalog.data.gov/dataset?q=&sort=metadata_created+desc');
text = ep_obj.downloader();
if ((str(text).lower()).find('html') != -1):
        ep_obj.parser(text);
        ep_obj.extractor_dataset_count();
        ep_obj.extractor_latest_dataset();
        ep_obj.json_converter();
    # os.system('clear');