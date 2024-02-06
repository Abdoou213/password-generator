# Password Generator

This project provides a simple yet powerful tool for generating secure passwords. It allows users to specify the length of the password and whether to include digits and/or special characters, making it versatile for various security needs. I used this project to get familiar with github actions and CI/CD workflows in Python.

## Features

- **Customizable Length**: Users can specify the desired length of the password, allowing for flexibility in balancing memorability and security.
- **Inclusion of Digits and Special Characters**: Enhance password security by optionally including digits and/or special characters.
- **User-friendly Interface**: Easy-to-follow prompts guide the user through the process of generating a password.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the password generator, ensure you have Python 3 installed on your system. You can download Python [here](https://www.python.org/downloads/).

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

### How to Use

To start generating a password, run the following command in the terminal:

```bash
python -m src.generator
```

Follow the on-screen prompts to customize your password. You will be asked to specify the length of the password and whether to include digits and/or special characters.

### Running the Tests

This project comes with a suite of unit tests to ensure functionality works as expected. To run the tests, execute:

```bash
python -m unittest test.unit_test
```

## Contributing

Contributions are welcome, and any contributions you make are **greatly appreciated**. Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
