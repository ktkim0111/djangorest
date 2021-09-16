from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import serializers, viewsets
from .serializer import CarSpecsSerializer
from firstApp.models import CarPlan, CarSpecs


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    print(request.query_params)
    print(request.query_params['num'])
    number = request.query_params['num']
    new_number = int(number) * 2
    return Response({"message": "we received your request", 'result': new_number})

# ViewSet 사용


class CarSpecsViewSet(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params)
    #     params_list = params['pk'].split('-')
    #     cars = CarSpecs.objects.filter(
    #         car_brand=params_list[0], car_model=params_list[1])
    #     serializer = CarSpecsSerializer(cars, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     car_data = request.data

    #     new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(id=car_data["car_plan"]),
    #                                       car_brand=car_data["car_brand"],
    #                                       car_model=car_data["car_model"],
    #                                       production_year=car_data["production_year"],
    #                                       car_body=car_data["car_body"],
    #                                       engine_type=car_data["engine_type"])

    #     new_car.save()

    #     serializer = CarSpecsSerializer(new_car)

    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     logedin_user = request.user
    #     if(logedin_user == "admin"):
    #         car = self.get_object()
    #         car.delete()
    #         response_message = {"message": "Item has been deleted"}
    #     else:
    #         response_message = {"message": "Not Allowed"}

    #     return Response(response_message)
