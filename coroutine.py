import asyncio

async def fetch_data(delay, id):
    print(f"Start fetching data {id}")
    await asyncio.sleep(delay)
    print(f"Done fetching data {id}")
    return {"data": f"Data {id}"}

async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Result 1: {result1}")

    result2 = await task2
    print(f"Result 2: {result2}")


asyncio.run(main())