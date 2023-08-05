from .gRPC_proto.user_proto import user_pb2, user_pb2_grpc


class Admin:
    def __init__(self, channel, metadata):
        self.stub = user_pb2_grpc.UserControllerStub(channel)
        self.metadata = metadata

    def create_user(self, params):
        response = self.stub.Create(
            user_pb2.User(username=params['username'], password=params['password'], email=params['email'],
                          first_name=params['first_name'], last_name=params['last_name']), metadata=self.metadata)
        return response

    def list_user(self):
        for post in self.stub.List(user_pb2.UserListRequest(), metadata=self.metadata):
            print(post, end='')

    def retrieve_user(self, id):
        response = self.stub.Retrieve(user_pb2.UserRetrieveRequest(id=id), metadata=self.metadata)
        return response

    def update_user(self, params):
        response = self.stub.Update(
            user_pb2.User(username=params['username'], password=params['password'], email=params['email'],
                          first_name=params['first_name'], last_name=params['last_name']), metadata=self.metadata)
        return response

    def delete_user(self, params):
        response = self.stub.Destroy(
            user_pb2.User(username=params['username'], password=params['password'], email=params['email'],
                          first_name=params['first_name'], last_name=params['last_name']), metadata=self.metadata)
        return response

    def add_access(self, params):
        response = self.stub.AddAccess(
            user_pb2.UserRequest(username=params['username'], access=params['access']), metadata=self.metadata)
        return response

    def remove_access(self, params):
        response = self.stub.RemoveAccess(
            user_pb2.UserRequest(username=params['username'], access=params['access']), metadata=self.metadata)
        return response
