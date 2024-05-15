import asyncio

async def fetch_data(id, sleeps):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleeps)
    return {"id": id, "data": f"Sample Data {id}"}

async def main():

    # task1 = asyncio.create_task(fetch_data(1, 2))
    # task2 = asyncio.create_task(fetch_data(2, 3))
    # task3 = asyncio.create_task(fetch_data(3, 1))

    # result1 = await task1
    # result2 = await task2
    # result3 = await task3

    # print(result1, result2, result3)

    # results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))


    tasks = []
    async with asyncio.TaskGroup() as group:
        for i, sleeps in enumerate([2,1,3], start=1):
            task = group.create_task(fetch_data(i, sleeps))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())