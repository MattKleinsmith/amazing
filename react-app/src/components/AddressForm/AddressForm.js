import styles from './AddressForm.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from 'react-router-dom';

import { getAddresses, postAddress, putAddress } from '../../store/addresses';

export default function AddressForm() {
    const { addressId } = useParams();
    const address = useSelector(state => state.addresses)[addressId];
    const dispatch = useDispatch();

    const regionField = useRef();
    const [region, setRegion] = useState(address?.region || "");
    const [regionError, setRegionError] = useState("");

    const fullnameField = useRef();
    const [fullname, setFullname] = useState(address?.fullname || "");
    const [fullnameError, setFullnameError] = useState("");

    const addressField = useRef();
    const [addressValue, setAddressValue] = useState(address?.address || "");
    const [addressValueError, setAddressValueError] = useState("");

    const buildingNumberField = useRef();
    const [buildingNumber, setBuildingNumber] = useState(address?.buildingNumber || "");
    const [buildingNumberError, setBuildingNumberError] = useState("");

    const cityField = useRef();
    const [city, setCity] = useState(address?.city || "");
    const [cityError, setCityError] = useState("");

    const stateField = useRef();
    const [state, setState] = useState(address?.state || "");
    const [stateError, setStateError] = useState("");

    const zipcodeField = useRef();
    const [zipcode, setZipcode] = useState(address?.zipcode || "");
    const [zipcodeError, setZipcodeError] = useState("");

    const phoneNumberField = useRef();
    const [phoneNumber, setPhoneNumber] = useState(address?.phoneNumber || "");
    const [phoneNumberError, setPhoneNumberError] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        if (addressId && !address) {
            dispatch(getAddresses());
        }
    }, [addressId, address, dispatch]);

    useEffect(() => {
        setRegion(address?.region || "");
        setFullname(address?.fullname || "");
        setAddressValue(address?.address || "");
        setBuildingNumber(address?.buildingNumber || "");
        setCity(address?.city || "");
        setState(address?.state || "");
        setZipcode(address?.zipcode || "");
        setPhoneNumber(address?.phoneNumber || "");
    }, [address])

    useEffect(() => {
        regionField.current.focus();
    }, []);

    const onClickContinue = async () => {
        let hasErrors = false;

        if (!phoneNumber) {
            setPhoneNumberError("Please enter a phone number so we can call if there are any issues with delivery.");
            phoneNumberField.current.focus();
            hasErrors = true;
        }

        if (!zipcode) {
            setZipcodeError("Please enter a ZIP or postal code.");
            zipcodeField.current.focus();
            hasErrors = true;
        }

        if (!city) {
            setCityError("Please enter a city name.");
            cityField.current.focus();
            hasErrors = true;
        }

        if (!addressValue) {
            setAddressValueError("Please enter an address.");
            addressField.current.focus();
            hasErrors = true;
        }

        if (!fullname) {
            setFullnameError("Please enter a name.");
            fullnameField.current.focus();
            hasErrors = true;
        }

        if (!region) {
            setRegionError("Please enter a region");
            regionField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;

        try {
            const body = { region, fullname, address: addressValue, city, state, zipcode }
            const productThunkAction = address ? putAddress(addressId, body) : postAddress(body);
            await dispatch(productThunkAction);
        }
        catch (responseBody) {
            console.log(responseBody);
        }
        navigate("/addresses");
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    return (
        <>
            <div className={styles.wrapper}>

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.heading}>{addressId ? "Edit your" : "Add a new"} address</div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormRegion" className={styles.fieldLabel}>
                            Country/Region
                        </label>
                        <input
                            ref={regionField}
                            id="addressFormRegion"
                            className={`${styles.fieldInput} ${regionError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={region}
                            onChange={(e) => {
                                setRegionError("");
                                setRegion(e.target.value);
                            }}
                        />
                        {regionError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{regionError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormName" className={styles.fieldLabel}>
                            Full name (First and Last name)
                        </label>
                        <input
                            ref={fullnameField}
                            id="addressFormName"
                            className={`${styles.fieldInput} ${fullnameError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={fullname}
                            onChange={(e) => {
                                setFullnameError("");
                                setFullname(e.target.value);
                            }}
                        />
                        {fullnameError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{fullnameError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormAddress" className={styles.fieldLabel}>
                            Street address
                        </label>
                        <input
                            ref={addressField}
                            id="addressFormAddress"
                            className={`${styles.fieldInput} ${addressValueError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={addressValue}
                            placeholder="Street address, P.O. box, company name, c/o"
                            onChange={(e) => {
                                setAddressValueError("");
                                setAddressValue(e.target.value);
                            }}
                        />
                        {addressValueError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{addressValueError}</div>
                        </div>}
                        <input
                            ref={buildingNumberField}
                            className={`${styles.fieldInput} ${buildingNumberError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={buildingNumber}
                            placeholder="Apartment, suite, unit, building, floor, etc."
                            onChange={(e) => {
                                setBuildingNumberError("");
                                setBuildingNumber(e.target.value);
                            }}
                        />
                    </div>


                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormCity" className={styles.fieldLabel}>
                            City
                        </label>
                        <input
                            ref={cityField}
                            id="addressFormCity"
                            className={`${styles.fieldInput} ${cityError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={city}
                            onChange={(e) => {
                                setCityError("");
                                setCity(e.target.value);
                            }}
                        />
                        {cityError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{cityError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormState" className={styles.fieldLabel}>
                            State / Province / Region
                        </label>
                        <input
                            ref={stateField}
                            id="addressFormState"
                            className={`${styles.fieldInput} ${stateError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={state}
                            onChange={(e) => {
                                setStateError("");
                                setState(e.target.value);
                            }}
                        />
                        {stateError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{stateError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormZipcode" className={styles.fieldLabel}>
                            Zip Code
                        </label>
                        <input
                            ref={zipcodeField}
                            id="addressFormZipcode"
                            className={`${styles.fieldInput} ${zipcodeError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={zipcode}
                            onChange={(e) => {
                                setZipcodeError("");
                                setZipcode(e.target.value);
                            }}
                        />
                        {zipcodeError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{zipcodeError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="addressFormPhoneNumber" className={styles.fieldLabel}>
                            Phone number
                        </label>
                        <input
                            ref={phoneNumberField}
                            id="addressFormPhoneNumber"
                            className={`${styles.fieldInput} ${phoneNumberError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={phoneNumber}
                            onChange={(e) => {
                                setPhoneNumberError("");
                                setPhoneNumber(e.target.value);
                            }}
                        />
                        {phoneNumberError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{phoneNumberError}</div>
                        </div>}
                    </div>

                    <button type="submit" className={`${styles.continue} ${styles.noselect}`}>Add address</button>
                </form>
            </div>
        </>
    );
}