from douyin.structures import Video
from douyin.handlers import Handler
from douyin.downloaders import Downloader


class VideoDownloader(Downloader):
    
    def process_item(self, obj):
        """
        process item
        :param obj: single obj
        :return:
        """
        if isinstance(obj, Video):
            print('\nDownloading', obj, '...')
            for handler in self.handlers:
                if isinstance(handler, Handler):
                    handler.process(obj.play_url, obj.id)
