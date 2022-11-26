import asyncio
import logging
import os
from collections import defaultdict
from datetime import datetime

import grpc
from requests import get

import slugs.server_pb2_grpc
from slugs.server_pb2 import HelloRequest, HelloResponse, TimeResponse, TimeRequest, GeoRequest, GeoResponse
from slugs.server_pb2_grpc import add_CurrentTimestampServicer_to_server, CurrentTimestampServicer, \
    add_GuessCountryServicer_to_server, GuessCountryServicer
from slugs.sum_pb2 import SumRequest, ExactSumReqeust, SumResponse, ExactSumResponse, GeneralError, OneOfResepone
from slugs.sum_pb2_grpc import ManySumServicer, add_ManySumServicer_to_server

os.environ.setdefault('GRPC_VERBOSITY', 'debug')


class ManySumServicer(slugs.sum_pb2_grpc.ManySumServicer):
    async def sumToTarget(self, request: SumRequest, context) -> SumResponse:
        if request.target_number is not None:
            acc = 0
            for x in range(request.target_number):
                acc += x
                yield SumResponse(sum_number=acc)
        else:
            yield SumResponse(error=GeneralError(message='I did not get any number!'))

    async def exactSum(self, request: ExactSumReqeust, context) -> ExactSumResponse:
        if request.target_number is not None:
            result = 0
            sta = defaultdict(int)
            for num in request.target_number:
                result += num
                sta[num] += 1

            return ExactSumResponse(sum_number=result, statistic=sta)
        else:
            return ExactSumResponse(error=GeneralError('I did not get any number!'))

    async def testOneOf(self, request_iterator, context):
        async for new_request in request_iterator:
            new_request: HelloRequest

            if new_request.name == 'hello':
                yield OneOfResepone(name=new_request.name)
            elif new_request.name == 'world':
                yield OneOfResepone(number=13)
            else:
                yield OneOfResepone(error=GeneralError(message="please input \"hello\" or \"world\""))


class GuessCountryServicer(slugs.server_pb2_grpc.GuessCountryServicer):
    async def geo(self, request_iterator, context):
        print(f'{request_iterator=}')
        async for new_geo in request_iterator:
            if type(new_geo) == GeoRequest:
                new_geo: GeoRequest
                print(f'{new_geo=}')
                lat = new_geo.latitude
                lon = new_geo.longitude
                g = get(f'http://api.geonames.org/countryCodeJSON?lat={lat}&lng={lon}&username=kreimben')
                country_name = g.json().get("countryName")

                print(f'{country_name=} {lon=} {lat=}')

                yield GeoResponse(country_name=country_name)


class CurrentTimestampServicer(slugs.server_pb2_grpc.CurrentTimestampServicer):
    async def getCurrentTime(self, request: TimeRequest, context):
        if request.timezone:
            dt = datetime.now()
        else:
            dt = datetime.utcnow()
        return TimeResponse(current_time=str(dt), tz=request.timezone)

    async def sayHello(self, request: HelloRequest, context):
        res = None
        print(f'received: {request=}')
        if request.name:
            res = HelloResponse(message=f'Hello, {request.name}')
        else:
            res = HelloResponse(message=f'Hello, Unknown')

        return res


async def server_init():
    print(f'server start!')
    server = grpc.aio.server()
    add_CurrentTimestampServicer_to_server(
        CurrentTimestampServicer(), server
    )
    add_GuessCountryServicer_to_server(
        GuessCountryServicer(), server
    )
    add_ManySumServicer_to_server(
        ManySumServicer(), server
    )
    server.add_insecure_port('localhost:5000')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(server_init())
