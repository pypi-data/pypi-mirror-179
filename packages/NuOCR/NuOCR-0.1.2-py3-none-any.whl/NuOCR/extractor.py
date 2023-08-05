import grpc, json
from .gRPC_proto.extractor_APIs_proto import extractor_pb2, extractor_pb2_grpc


class Extractor:
    def __init__(self, channel, metadata):
        self.stub = extractor_pb2_grpc.ExtractorControllerStub(channel)
        self.metadata = metadata

    def form_recognizer(
            self,
            fileName,
            inputType,
            extractionType,
            url='',
            base64='',
            pages=None,
            mimeType='application/pdf',
            rawJson=False,
            language=''
    ):
        try:
            request = extractor_pb2.FormRequest(language=language,
                                                inputType=inputType,
                                                fileName=fileName,
                                                url=url,
                                                base64=base64,
                                                pages=pages,
                                                mimeType=mimeType,
                                                extractionType=extractionType,
                                                rawJson=rawJson)
            response = self.stub.FormRecognition(request, metadata=self.metadata)
            return json.loads(response.body)
        except grpc.RpcError as e:
            raise Exception('Error ' + str(e.code()) + ': ' + str(e.details()))

    def doc_recognizer(
            self,
            fileName,
            inputType,
            extractionType,
            url='',
            base64='',
            mimeType='application/pdf',
            extractionHints=False,
            rawJson=False,
    ):
        try:
            request = extractor_pb2.DocRequest(
                fileName=fileName,
                inputType=inputType,
                url=url,
                base64=base64,
                mimeType=mimeType,
                extractionType=extractionType,
                extractionHints=extractionHints,
                rawJson=rawJson
            )
            response = self.stub.DocAI(request, metadata=self.metadata)
            return json.loads(response.body)
        except grpc.RpcError as e:
            raise Exception('Error ' + str(e.code()) + ': ' + str(e.details()))

    def vin_extractor(
            self,
            fileName,
            inputType,
            extractionType='vin',
            url='',
            base64='',
            preProcessors=[],
            mimeType='application/pdf',
            rawJson=False,
            language='',
    ):
        try:
            request = extractor_pb2.VinRequest(language=language,
                                               inputType=inputType,
                                               fileName=fileName,
                                               url=url,
                                               base64=base64,
                                               preProcessors=preProcessors,
                                               mimeType=mimeType,
                                               extractionType=extractionType,
                                               rawJson=rawJson)
            response = self.stub.VinNumber(request, metadata=self.metadata)
            return json.loads(response.body)
        except grpc.RpcError as e:
            raise Exception('Error ' + str(e.code()) + ': ' + str(e.details()))
