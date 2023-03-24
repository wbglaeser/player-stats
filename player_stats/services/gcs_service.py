from google.cloud import storage


class GcsService:
    GOOGLE_CREDENTIALS = "config/player-stats-credentials.json"
    BUCKET_NAME = "player-stats"

    def __init__(self):
        self.client = storage.Client.from_service_account_json(self.GOOGLE_CREDENTIALS)
        self.bucket = self.client.get_bucket(self.BUCKET_NAME)

    @classmethod
    def upload(cls, file_name, file_path):
        gcs_service = cls()
        blob = gcs_service.bucket.blob(file_name)
        blob.upload_from_filename(file_path)

    @classmethod
    def download(cls, file_name, file_path):
        gcs_service = cls()
        blob = gcs_service.bucket.blob(file_name)
        blob.download_to_filename(file_path)

    @classmethod
    def list(cls):
        gcs_service = cls()
        return gcs_service.client.list_blobs(cls.BUCKET_NAME)


if __name__ == "__main__":
    GcsService.upload("test.txt", "test.txt")
    print(list(GcsService.list()))
