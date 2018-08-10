from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['yob'])

id_to_find = "5b5b1ed4b38f670ee85bf765"
# kết quả trả ra 1 object
# service = Service.objects.get(id=id_to_find)

# kết quả trả ra 1 object
service = Service.objects.with_id(id_to_find)
# print(service.to_mongo())

# ## delete
# check document is exist or not
if service is not None:
    # service.delete()
    # print("Delete")

    # ## Update
    print("Before", service.to_mongo())
    service.update(set__name="Anh", set__yob=2000)
    service.reload()
    print("After", service.to_mongo())
else:
    print("Not found")