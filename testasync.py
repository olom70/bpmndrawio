import asyncio
import aiohttp
import time

words = ["hello", "mellow", "cat", "rat", "dog", "frog", "mouse", "sparrow", "man", "women"]


def merge_lists(results_from_fc):
    """
    Function for merging multiple lists
    """
    combined_list = []
    for li in results_from_fc:
        combined_list.extend(li)

async def get_rhyming_words(session, word):
    url = f"https://api.datamuse.com/words?rel_rhy={word}&max=1000"
    async with session.get(url) as response:
        result_data = await response.json()
        return result_data

async def main():
    headers = {'content-type': 'application/json'}
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for word in words:
            task = asyncio.ensure_future(get_rhyming_words(session, word))
            tasks.append(task)
        all_results = await asyncio.gather(*tasks)
        combined_list = merge_lists(all_results)
        return combined_list

async_func_start_time = time.time()
response2 = asyncio.get_event_loop().run_until_complete(main())
time_with_async = time.time() - async_func_start_time
print("\nTotal time with async/await execution >> ", time_with_async, " seconds")
print(response2)