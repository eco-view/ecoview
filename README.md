<img width="1440" alt="Screen Shot 2019-03-10 at 6 48 19 AM" src="https://user-images.githubusercontent.com/46664545/54083926-90358b80-4300-11e9-980c-6169ab2a98df.png">

# :recycle: ecoview :recycle:

Cloud-based recycling module with object classification

UB Electrical Engineering Capstone Design, Spring 2019
- Software Lead: Michael Lawrenson
- Image Acquisition Lead: Osama Abaali
- Peripherals Lead: Lee Yanting
- Microcontroller Lead: Justin Struzik

## Getting Started

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

todo

## Built With

* [Python](https://www.python.org/) - Primary language
* [Flask](http://flask.pocoo.org/) - Web framework
* [MySQL](https://www.mysql.com/) - Database
* [Tensorflow](https://www.tensorflow.org/) - Image processing
* [Bootstrap](https://getbootstrap.com/) - Visual styling

## Contributing

This project was created for use within our Capstone project and will not be accepting pull requests from outside individuals.

## Versioning

ecoview:latest

## Authors

* **Michael Lawrenson** - *Software Lead* - [minelminel](https://github.com/minelminel)
* **Osama Abaali** - *Image Lead* - [PurpleBooth](https://github.com/PurpleBooth)
* **Lee Yanting** - *IPeripherals Lead* - [PurpleBooth](https://github.com/PurpleBooth)
* **Justin Struzik** - *Microcontroller Lead* - [PurpleBooth](https://github.com/PurpleBooth)



### Overview
- Abstract
- Architecture
- Setup

### Stack
- Website
– Database
- Image Processing
- Communication

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* much love to the folks at StackOverflow

