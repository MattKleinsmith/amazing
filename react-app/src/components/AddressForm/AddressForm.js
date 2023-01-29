import styles from './AddressForm.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useNavigate, useParams, useSearchParams } from 'react-router-dom';

import { getAddresses, postAddress, putAddress } from '../../store/addresses';
import { setAddressModal, setBuyModal } from '../../store/ui';

export default function AddressForm({ isModal = false }) {
    const { addressId } = useParams();
    const searchParams = useSearchParams()[0];
    const productId = searchParams.get('productId');
    const quantity = searchParams.get('quantity');
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

    const buildingField = useRef();
    const [building, setBuildingNumber] = useState(address?.building || "");
    const [buildingError, setBuildingNumberError] = useState("");

    const cityField = useRef();
    const [city, setCity] = useState(address?.city || "");
    const [cityError, setCityError] = useState("");

    const stateField = useRef();
    const [state, setState] = useState(address?.state || "");
    const [stateError, setStateError] = useState("");

    const zipcodeField = useRef();
    const [zipcode, setZipcode] = useState(address?.zipcode || "");
    const [zipcodeError, setZipcodeError] = useState("");

    const phoneField = useRef();
    const [phone, setPhoneNumber] = useState(address?.phone || "");
    const [phoneError, setPhoneNumberError] = useState("");

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
        setBuildingNumber(address?.building || "");
        setCity(address?.city || "");
        setState(address?.state || "");
        setZipcode(address?.zipcode || "");
        setPhoneNumber(address?.phone || "");
    }, [address])

    useEffect(() => {
        regionField.current.focus();
    }, []);

    const onClickContinue = async () => {
        let hasErrors = false;

        if (!/^\d{10}$/.test(phone)) {
            setPhoneNumberError("Please enter a phone number so we can call if there are any issues with delivery.");
            phoneField.current.focus();
            hasErrors = true;
        }

        if (zipcode.length < 5 || zipcode.length > 10) {
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

        let shouldNavigate = true;
        try {
            const body = { region, fullname, address: addressValue, city, state, zipcode, phone, building }
            const productThunkAction = address ? putAddress(addressId, body) : postAddress(body);
            await dispatch(productThunkAction);
            if (productId) {
                dispatch(setBuyModal(true, productId, quantity));
                navigate(`/listing/${productId}`);
                shouldNavigate = false;
            }
            else if (isModal) {
                dispatch(setAddressModal(false));
                shouldNavigate = false;
            }
        }
        catch (responseBody) {
            console.log(responseBody);
        }
        if (shouldNavigate) navigate("/addresses");
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    return (
        <>
            <div className={isModal ? styles.wrapperModal : styles.wrapper}>
                {!isModal && <div className={styles.navInfo}>Your Account {">"} <NavLink to="/addresses" className={styles.yourAddresses}>Your Addresses</NavLink> {">"} <span className={styles.youAreHere}>{addressId ? "Edit" : "New"} Address</span></div>}
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
                            ref={buildingField}
                            className={`${styles.fieldInput} ${buildingError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={building}
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
                            ref={phoneField}
                            id="addressFormPhoneNumber"
                            className={`${styles.fieldInput} ${phoneError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={phone}
                            onChange={(e) => {
                                setPhoneNumberError("");
                                setPhoneNumber(e.target.value);
                            }}
                        />
                        {phoneError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{phoneError}</div>
                        </div>}
                    </div>

                    <button type="submit" className={`${styles.continue} ${styles.noselect}`}>{addressId ? "Edit" : "Add"} address</button>
                </form>
            </div>
        </>
    );
}
