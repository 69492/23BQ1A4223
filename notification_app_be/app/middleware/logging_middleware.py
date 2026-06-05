import time


class LoggingMiddleware:

    async def __call__(self, request, call_next):

        start_time = time.time()

        print("=" * 50)
        print(f"Method : {request.method}")
        print(f"URL    : {request.url}")

        response = await call_next(request)

        process_time = time.time() - start_time

        print(f"Status : {response.status_code}")
        print(f"Time   : {process_time:.4f} sec")
        print("=" * 50)

        return response