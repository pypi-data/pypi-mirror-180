import contextlib
import socket
import asyncio


async def check_internet_connection() -> bool:
    def _check_connection() -> bool:
        with contextlib.suppress(OSError):
            conn = socket.create_connection(("www.google.com", 80))
            conn.close()

            return True

        return False

    loop = asyncio.get_event_loop()

    return await loop.run_in_executor(None, _check_connection)


async def print_result() -> None:
    print(await check_internet_connection())


if __name__ == '__main__':
    asyncio.run(print_result())
