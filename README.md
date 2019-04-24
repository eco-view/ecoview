# :recycle: ecoview :recycle:

Cloud-based recycling module with object classification

<img width="1440" alt="Screen Shot 2019-03-10 at 6 48 19 AM" src="https://user-images.githubusercontent.com/46664545/54083926-90358b80-4300-11e9-980c-6169ab2a98df.png">


UB Electrical Engineering Capstone Design, Spring 2019
- Software Lead: Michael Lawrenson
- Image Acquisition Lead: Osama Abaali
- Peripherals Lead: Lee Yanting
- Microcontroller Lead: Justin Struzik

## Overview
#### Abstract
Raspberry Pi integrated with a compartmentalized recycling station, capable of monitoring deposits in individual *totes*, measuring the height of *tote* contents, and relaying this information to our web app via our API. In addition, the user can capture a photo of their recycleable and provide a categorical assignment by examining the symbol located on the underside. This resulting collection of crowdsourced images is aggregated and used as training data for our convolution neural network, or *CNN*.
#### Architecture
Content height is measured with ultrasonic sensors, which measure the time needed to echo a trigger signal. Deposits are registed by means of continuosly monitored infrared break beams. At regular time intervals, collected information stored in-memory is used to construct an API request, syncronizing the web app with the physical system. Image files are stored in a heirarchy such that directory names are the ground-truth classification labels.
#### Setup
There are 3 main program branches:
- Firmware, run locally on the Pi
- Web app, run in a Docker container
- Image Analysis, eventually to be performed with Google Colaboratory

## Stack
#### Website
- Framework: Flask
- Styling: Bootstrap
- Graphics: Chartist.js
#### Database
- MySQL
#### Image Processing
- Tensorflow
#### Communication
- restful API:  ecoview.stateData(), ecoview.processData()


## Overview

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Real-world deployement performed with Docker.

### Installing

Clone the repository to a local directory

```
  git clone https://github.com/eco-view/ecoview.git
```

### Dependencies

Make sure you have all the required python modules
```
  pip3 install -r requirements.txt
```

Initialize SQL database

```
  mysql.server start
```

Start the flask server

```
  python3 app.py
```

By default, the server will run on port 8080

```
  http://localhost:8080/
```


## Deployment

```
docker build ecoview:latest .
docker run -d -p 8080:8080 ecoview:latest
echo 'Running [ecoview] @ http://localhost:8080
```

## Built With

* [Python](https://www.python.org/) - Primary language
* [Flask](http://flask.pocoo.org/) - Web framework
* [MySQL](https://www.mysql.com/) - Database
* [Tensorflow](https://www.tensorflow.org/) - Image processing
* [Bootstrap](https://getbootstrap.com/) - Visual styling

## Contributing

*no outside contribution*

## Versioning

ecoview:latest

## Author

* **Michael Lawrenson** - *Software Lead* - [minelminel](https://github.com/minelminel)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* much love to the folks at StackOverflow

