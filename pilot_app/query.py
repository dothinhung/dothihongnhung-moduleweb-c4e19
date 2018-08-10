from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()

