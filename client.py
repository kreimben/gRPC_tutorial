import asyncio
import random

import grpc

from slugs import server_pb2_grpc, sum_pb2_grpc
from slugs.server_pb2 import HelloRequest, TimeRequest, GeoRequest, GeoResponse
from slugs.sum_pb2 import SumResponse, ExactSumReqeust, OneOfResepone, SumRequest


async def say_hello(channel):
    print(f'say_hello')
    # guess_country_stub = server_pb2_grpc.GuessCountryStub(channel)
    current_timestamp_stub = server_pb2_grpc.CurrentTimestampStub(channel)

    feature_future = current_timestamp_stub.sayHello(
        HelloRequest(name="Kreimben")
    )

    print(f'{feature_future}')


async def get_current_time(channel):
    print(f'get_current_time')
    current_timestamp_stub = server_pb2_grpc.CurrentTimestampStub(channel)

    feature_future = current_timestamp_stub.getCurrentTime(
        TimeRequest(timezone='Asia/Seoul')
    )

    print(f'{feature_future}')


async def geo(channel):
    print(f'geo')
    guess_country_stub = server_pb2_grpc.GuessCountryStub(channel)
    req = [GeoRequest(latitude=random.randint(-90, 90), longitude=random.randint(-180, 180)) for _ in range(5)]
    results = []

    async for feature in guess_country_stub.geo(iter(req)):
        if feature.country_name:
            results.append(feature.country_name)

    print(f'{results=}')


async def sum_to_target(channel):
    print(f'sum_to_target')
    many_sum_stub = sum_pb2_grpc.ManySumStub(channel)

    async for feature in many_sum_stub.sumToTarget(SumRequest(target_number=11)):
        feature: SumResponse
        print(f'{feature.sum_number=}')


async def exact_sum(channel):
    print(f'exact_sum')
    many_sum_stub = sum_pb2_grpc.ManySumStub(channel)
    data = [1, 1, 1, 1, 2, 3, 4, 1, 5, 7, 4, 7, 34, 2, 2]
    print(f'ready {data=}')
    feature = many_sum_stub.exactSum(ExactSumReqeust(target_number=data))
    print(f'success {feature=}')


async def test_one_of(channel):
    print(f'test_one_of')
    many_sum_stub = sum_pb2_grpc.ManySumStub(channel)

    data = [HelloRequest(name='1241'), HelloRequest(name='sldkg'), HelloRequest(name='hello'),
            HelloRequest(name='world')]

    async for feature in many_sum_stub.testOneOf(iter(data)):
        feature: OneOfResepone
        print(f'{feature=}')
        if feature.name is not None:
            print(f'{feature.name=}')
        elif feature.number is not None:
            print(f'{feature.number=}')
        elif feature.error is not None:
            print(f'{feature.error=}')


async def main():
    channel = grpc.aio.insecure_channel('localhost:5000')
    await say_hello(channel)
    await get_current_time(channel)
    await geo(channel)
    await sum_to_target(channel)
    await exact_sum(channel)
    await test_one_of(channel)


if __name__ == '__main__':
    asyncio.run(main())
