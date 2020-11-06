all: begin_message installation_protocol

begin_message:
	@echo "Installing QGOL..."

installation_protocol:
	@pip3 install -r requirements.txt --user
	@echo "Installation complete. Please type \"python3 test.py\" to start the tests."

clean:
	@echo "The project is already clean."


