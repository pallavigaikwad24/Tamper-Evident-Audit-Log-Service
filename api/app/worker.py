import asyncio

async def main():
    while True:
        print("verifier Tick")
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())