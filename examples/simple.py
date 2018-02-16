import asyncio
from datetime import datetime

from seppuku import killme_after

loop = asyncio.get_event_loop()


def run():
    start_time = datetime.now()
    print('Started')

    killme_after(2, loop)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt after {}'.format(datetime.now() - start_time))


if __name__ == '__main__':
    run()
