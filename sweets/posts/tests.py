from django.test import Client
from django.test import TestCase
from .models import Orders,Couriers
# Create your tests here.

courier_data = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },
        {
            "courier_id": 2,
            "courier_type": "bike",
            "regions": [22],
            "working_hours": ["09:00-18:00"]
        },
        {
            "courier_id": 3,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        },
        {
            "courier_id": 4,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        }
    ]
}

data_complete_cour = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },

        {
            "courier_id": 2,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        }
    ]
}
data_complete_order={
"courier_id": 1,
"order_id": 1,
"complete_time": "2021-01-10T10:33:01.42Z"
}

data_complete_order_invalid={
"courier_id": 2,
"order_id": 1,
"complete_time": "2021-01-10T10:33:01.42Z"
}


courier_data_invalid_field_val = {
    "data": [
        {
            "courier_id": 11,
            "courier_type": "foot",
            "regions": "22",
            "working_hours": ["11:35-14:05", "09:00-11:00"]
        },
        {
            "courier_id": 11,
            "courier_type": "bike",
            "regions": [22],
            "working_hours": ["09:00-18:00"]
        },
        {
            "courier_id": 3,
            "courier_type": "car",
            "regions": [12, 22, 23, 33],
            "working_hours": []
        }
    ]
}

courier_data_field_mistake = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
        }
    ]
}

courier_data_patch = {
    "data": [
        {
            "courier_id": 1,
            "courier_type": "foot",
            "regions": [1, 12, 22],
            "working_hours": ["09:00-18:00"]
        }
    ]
}
data_patch = {"courier_type": "car"}
data_patch_invalid = {"blabla": [22]}
data_patch_invalid_2 = {"courier_type"}
data_assign ={
"courier_id": 1
}

data_assign_2 ={
"courier_id": 123
}
data_complete = {
"courier_id": 1,
"order_id": 1,
"complete_time": "2021-01-10T10:33:01.42Z"
}

data_complete_invalid = {
"courier_id": 2,
"order_id": 1,
"complete_time": "2021-01-10T10:33:01.42Z"
}
data_complete_invalid_2 = {
"courier_id": 2,
"order_id": 98,
"complete_time": "2021-01-10T10:33:01.42Z"
}
data_complete_invalid_3 = {
"courier_id": 1,
"order_id": 198,
"complete_time": "2021-01-10T10:33:01.42Z"
}

order_data = {
    "data": [
        {
            "order_id": 1,
            "weight": 0.23,
            "region": 12,
            "delivery_hours": ["09:00-18:00"]
        },
        {
            "order_id": 2,
            "weight": 15,
            "region": 22,
            "delivery_hours": ["09:00-18:00"]
        },
        {
            "order_id": 3,
            "weight": 0.01,
            "region": 22,
            "delivery_hours": ["09:00-12:00", "16:00-21:30"]
        }
    ]
}


order_data_add = {
    "data": [
        {
            "order_id": 123,
            "weight": 0.23,
            "region": 12,
            "delivery_hours": ["09:00-18:00"]
        }]}


order_data_invalid_field_val = {
    "data": [
        {
            "order_id": 11,
            "weight": ["0.23"],
            "region": "12",
            "delivery_hours": ["09:00-18:00"]
        },
        {
            "order_id": 16,
            "weight": 15,
            "region": 22,
            "delivery_hours": ["09:00-18:00"]
        }
    ]
}

order_data_field_mistake = {
    "data": [
        {
            "order_id": 1,
            "weight": 0.23,
            "delivery_hours": ["09:00-18:00"]
        }]}


class CourierTest(TestCase):
    def test_create(self):
        c = Client()
        response = c.post('/couriers', courier_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_invalid(self):
        c = Client()
        response_not_valid_repid = c.post('/couriers', courier_data_invalid_field_val, content_type='application/json')
        self.assertEqual(response_not_valid_repid.status_code, 400)
        response_not_valid = c.post('/couriers', courier_data_field_mistake, content_type='application/json')
        self.assertEqual(response_not_valid.status_code, 400)

    def test_patch(self):
        c = Client()
        response_patch_create = c.post('/couriers', courier_data_patch, content_type='application/json')
        self.assertEqual(response_patch_create.status_code, 201)
        response_patch = c.patch('/couriers/1', data_patch, content_type='application/json')
        self.assertEqual(response_patch.status_code, 200)

    def test_patch_invalid(self):
        c = Client()
        response_patch_create = c.post('/couriers', courier_data_patch, content_type='application/json')
        self.assertEqual(response_patch_create.status_code, 201)
        response_patch_invalid = c.patch('/couriers/1', data_patch_invalid, content_type='application/json')
        self.assertEqual(response_patch_invalid.status_code, 400)
        response_patch_invalid = c.patch('/couriers/1', data_patch_invalid_2, content_type='application/json')
        self.assertEqual(response_patch_invalid.status_code, 400)


class OrderTest(TestCase):
    def test_create(self):
        c = Client()
        response = c.post('/orders', order_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_invalid(self):
        c = Client()
        response_not_valid = c.post('/orders', order_data_invalid_field_val, content_type='application/json')
        self.assertEqual(response_not_valid.status_code, 400)
        response_not_valid = c.post('/orders', order_data_field_mistake, content_type='application/json')
        self.assertEqual(response_not_valid.status_code, 400)

    def test_assign(self):
        c = Client()
        response_patch_create = c.post('/couriers', courier_data_patch, content_type='application/json')
        self.assertEqual(response_patch_create.status_code, 201)
        response = c.post('/orders', order_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = c.post('/orders/assign', data_assign, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'"orders":[{"id":1},{"id":3}]')


    def test_assign_invalid(self):
        c = Client()
        response = c.post('/orders/assign', data_assign_2, content_type='application/json')
        self.assertEqual(response.status_code, 400)

class CompleteTest(TestCase):
    def setUp(self) -> None:
        c = Client()
        response_patch_create = c.post('/couriers', data_complete_cour, content_type='application/json')
        self.assertEqual(response_patch_create.status_code, 201)
        response = c.post('/orders', order_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = c.post('/orders/assign', data_assign, content_type='application/json')
        self.assertEqual(response.status_code, 200)



    def test_complete(self):
        c = Client()
        response = c.post('/orders/complete', data_complete, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'{"order_id":1}')

        self.assertEqual(Orders.objects.get(pk = 1).complete,True)

    def test_assign_time(self):
        c = Client()
        response = c.post('/orders/complete', data_complete, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '{"order_id":1}')

        self.assertEqual(Orders.objects.get(pk=1).complete, True)
        old_assign_time = Orders.objects.get(pk=1).assign_time
        response = c.post('/orders', order_data_add, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = c.post('/orders/assign', data_assign, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(Orders.objects.get(pk=123).assign_time,old_assign_time)


    def test_complete_invalid(self):
        c = Client()
        response = c.post('/orders/complete', data_complete_invalid, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = c.post('/orders/complete', data_complete_invalid_2, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = c.post('/orders/complete', data_complete_invalid_3, content_type='application/json')
        self.assertEqual(response.status_code, 400)