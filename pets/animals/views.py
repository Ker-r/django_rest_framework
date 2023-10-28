# from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .serializers import AnimalSerializer
from .models import Animal, Category


class AnimalAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 1000


class AnimalViewSet(viewsets.ModelViewSet):
    # queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    pagination_class = AnimalAPIListPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Animal.objects.all()
        return Animal.objects.filter(pk=pk)

    # При detail=False выводится список записей, а при True - одна запись
    @action(methods=['get'], detail=True)
    # Метод должен возвращать JSON ответ
    def category(self, request, pk=None):
        # Прочитаем все категории
        cats = Category. objects.get(pk=pk)
        # возвращаем JSON словарь со значением в виде списка
        # берем из Category только name
        return Response({'cats': cats.name})


# class AnimalAPIView(generics.ListAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

# class AnimalAPIList(generics.ListCreateAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer


# class AnimalAPIUpdate(generics.UpdateAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer
#     authentication_classes = (TokenAuthentication, )


# class AnimalAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Animal.objects.all()
#     serializer_class = AnimalSerializer

# class AnimalAPIView(APIView):
#     def get(self, request):
#         # Формируется список из объектов класса
#         a = Animal.objects.all()
#         # Преобразует список в список из словарей
#         # и все это преобразуется в байтовую json строку
#         return Response({'posts': AnimalSerializer(a, many=True).data})

#     def post(self, request):
#         # Создаем сериализатор на основе данных, поступивших с POST запроса
#         # И распаковываем их с помощью data
#         serializer = AnimalSerializer(data=request.data)
#         # Проверяем корректность принятых данных из serializers.py
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})

#     # Args - позиционные аргументы
#     # Kwargs - именованные аргументы
#     def put(self, request, *args, **kwargs):
#         # Обращаемся к словарю kwargs, берем из него ключ pk
#         pk = kwargs.get("pk", None)
#         # Если ключ не присутствует, то возвращаем ответ
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         # Пробуем указаную запись из модели по ключу pk
#         try:
#             instance = Animal.objects.get(pk=pk)
#         # Если мы не можем выбрать запись
#         except:
#             return Response({"error": "object doesnt exists"})
#         # Если мы получили и ключ и запись по этому ключу
#         # В качестве аргументов передадим данные, которые нужны изменить
#         # и объект которую собираемся поменять
#         serializer = AnimalSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
