import photos
import ui
import dialogs
import io

from objc_util import ObjCClass, load_framework

load_framework('Vision')
VNRecognizeTextRequest = ObjCClass('VNRecognizeTextRequest')
VNImageRequestHandler = ObjCClass('VNImageRequestHandler')
VNDetectTextRectanglesRequest = ObjCClass('VNTextObservation')

# Prompts user to select photo from Camera or Photos app
selection = dialogs.alert('Get image', button1='Camera', button2='Photos')

language = ['en']
image = None

if selection == 1:
    image = photos.capture_image()
elif selection == 2:
    image = photos.pick_asset().get_image()

if image is not None:
    print('Recognizing text...\n')
    
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    image_data = buffer.getvalue()

    req = VNRecognizeTextRequest.alloc().init().autorelease()
    req.setRecognitionLanguages_(language)
    handler = VNImageRequestHandler.alloc().initWithData_options_(image_data, None).autorelease()

    success = handler.performRequests_error_([req], None)

    if success:
        for result in req.results():
            print(result.text())
    else:
        print('Problem recognizing text')

print('\n--program complete--')
