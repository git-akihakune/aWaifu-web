console.clear();
// Range Slider Properties.
// Fill : The trailing color that you see when you drag the slider.
// background : Default Range Slider Background
const sliderProps = {
	fill: "#0B1EDF",
	background: "rgba(255, 255, 255, 0.214)",
};

// Selecting the Range Slider container which will effect the LENGTH property of the password.
const slider = document.querySelector(".range__slider");

// Text which will show the value of the range slider.
const sliderValue = document.querySelector(".length__title");

// Using Event Listener to apply the fill and also change the value of the text.
slider.querySelector("input").addEventListener("input", event => {
	sliderValue.setAttribute("data-length", event.target.value);
	applyFill(event.target);
});
// Selecting the range input and passing it in the applyFill func.
applyFill(slider.querySelector("input"));
// This function is responsible to create the trailing color and setting the fill.
function applyFill(slider) {
	const percentage = (100 * (slider.value - slider.min)) / (slider.max - slider.min);
	const bg = `linear-gradient(90deg, ${sliderProps.fill} ${percentage}%, ${sliderProps.background} ${percentage +
			0.1}%)`;
	slider.style.background = bg;
	sliderValue.setAttribute("data-length", slider.value);
}

// Object of all the function names that we will use to create random letters of password
const randomFunc = {
	lower: getRandomLower,
	upper: getRandomUpper,
	number: getRandomNumber,
	symbol: getRandomSymbol,
};

// Random more secure value
function secureMathRandom() {
	return window.crypto.getRandomValues(new Uint32Array(1))[0] / (Math.pow(2, 32) - 1);
}

// Generator Functions
// All the functions that are responsible to return a random value taht we will use to create password.
function getRandomLower() {
	return String.fromCharCode(Math.floor(Math.random() * 26) + 97);
}
function getRandomUpper() {
	return String.fromCharCode(Math.floor(Math.random() * 26) + 65);
}
function getRandomNumber() {
	return String.fromCharCode(Math.floor(secureMathRandom() * 10) + 48);
}
function getRandomSymbol() {
	const symbols = '~!@#$%^&*()_+{}":?><;.,';
	return symbols[Math.floor(Math.random() * symbols.length)];
}

// Selecting all the DOM Elements that are necessary -->

// The Viewbox where the result will be shown
const resultEl = document.getElementById("result");
// The input slider, will use to change the length of the password
const lengthEl = document.getElementById("slider");

// Checkboxes representing the options that is responsible to create differnt type of password based on user
const uppercaseEl = document.getElementById("uppercase");
const lowercaseEl = document.getElementById("lowercase");
const numberEl = document.getElementById("number");
const symbolEl = document.getElementById("symbol");

// Button to generate the password
const generateBtn = document.getElementById("generate");
// Button to copy the text
const copyBtn = document.getElementById("copy-btn");
// Result viewbox container
const resultContainer = document.querySelector(".result");
// Text info showed after generate button is clicked
const copyInfo = document.querySelector(".result__info.right");
// Text appear after copy button is clicked
const copiedInfo = document.querySelector(".result__info.left");

// if this variable is true only then the copyBtn will appear, i.e. when the user first click generate the copyBth will interact.
let generatedPassword = false;

// Update Css Props of the COPY button
// Getting the bounds of the result viewbox container
let resultContainerBound = {
	left: resultContainer.getBoundingClientRect().left,
	top: resultContainer.getBoundingClientRect().top,
};
// This will update the position of the copy button based on mouse Position
resultContainer.addEventListener("mousemove", e => {
	return
});

// Copy Password in clipboard
copyBtn.addEventListener("click", () => {
	return
});

// When Generate is clicked Password id generated.
generateBtn.addEventListener("click", () => {
	const quantity = lengthEl.value;
	const largeImage = lowercaseEl.checked;
	const multiCulture = uppercaseEl.checked;
	const autoDownload = numberEl.checked;
	const breakTimeLimit = symbolEl.checked;

	// // Send POST request to /profile
	// fetch("/profile", {
	// 	method: "POST",
	// 	redirect: "follow",
	// 	mode: "cors",
	// 	crossDomain: true,
	// 	headers: {
	// 		"Content-Type": "application/json",
	// 	},
	// 	body: JSON.stringify({
	// 		quantity: quantity,
	// 		largeImage: largeImage,
	// 		multiCulture: multiCulture,
	// 		autoDownload: autoDownload,
	// 		breakTimeLimit: breakTimeLimit,
	// 	}),
	// }).then(res => {
	// 	console.log('Response:', res);
	// 	window.location.replace(res.url);
	// })
    // .catch(function(err) {
    //     console.info(err + " url: " + '/profile');
    // });

	$.ajax({
		url: "/profile",
		type: "POST",
		data: {
			quantity: quantity,
			largeImage: largeImage,
			multiCulture: multiCulture,
			autoDownload: autoDownload,
			breakTimeLimit: breakTimeLimit
		},
		success: function (response) {
			if (response.successFlag) {
				//Replace current location from the history via history API
				window.history.replaceState({}, 'foo', '/foo');
				window.location = "url of target location here if you want to send a get request";
				$("#form-id").submit();//if you want to post something up
			}
		}
	});

});

// Function responsible to generate password and then returning it.
function generatePassword(length, lower, upper, number, symbol) {
	let generatedPassword = "";
	const typesCount = lower + upper + number + symbol;
	const typesArr = [{ lower }, { upper }, { number }, { symbol }].filter(item => Object.values(item)[0]);
	if (typesCount === 0) {
		return "";
	}
	for (let i = 0; i < length; i++) {
		typesArr.forEach(type => {
			const funcName = Object.keys(type)[0];
			generatedPassword += randomFunc[funcName]();
		});
	}
	return generatedPassword.slice(0, length)
									.split('').sort(() => Math.random() - 0.5)
									.join('');
}

// function that handles the checkboxes state, so at least one needs to be selected. The last checkbox will be disabled.
function disableOnlyCheckbox(){
	// let totalChecked = [uppercaseEl, lowercaseEl, numberEl, symbolEl].filter(el => el.checked)
	// totalChecked.forEach(el => {
	// 	if(totalChecked.length == 1){
	// 		el.disabled = true;
	// 	}else{
	// 		el.disabled = false;
	// 	}
	// })
	return
}

[uppercaseEl, lowercaseEl, numberEl, symbolEl].forEach(el => {
	el.addEventListener('click', () => {
		disableOnlyCheckbox()
	})
})