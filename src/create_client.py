from dask.distributed import Client

class CreateClient:

    def __init__(self) -> None:
        self.client = Client(processes=False)
