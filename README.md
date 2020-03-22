# Quarantino
WirVsCorona hackathon webapp of Saufnasen. Quarantino aims at connecting elderly people or people without internet access to various local support platforms. The app supports volunteering telephone operators to find a matching helper for their telephone customers. The backend database serves as a directory of available support platforms and helpers associated with this platform. The telephone operator picks a helper and a platform for the job requested by the customer. Afterwards, the operator contacts the helper and provides information about the job inquiry of the elderly customer.

This idea is already implemented in production by [gemeinschaft.online](gemeinschaft.online). That is why we chose to discontinue the project before the end of the hackathon. This repository contains all planning and coding we did up to the point where we discovered the existing solution.

* Devpost project page: [https://devpost.com/software/quarantino-lvyoe4]
* Hackathon denomination: 01_010_analogeunterstützung_Quarantino

## run
* `cd backend`
* `pipenv install`
* `pipenv shell`
* `python quarantino.py`
* Access webapp in your browser at `http://localhost:5000`.

### dependencies:
* Flask
* Flask API
* planned: Vue.js for the frontend placement application.
