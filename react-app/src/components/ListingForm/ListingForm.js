import styles from './ListingForm.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, useNavigate } from 'react-router-dom';

export default function RegisterForm() {
    const dispatch = useDispatch();

    const [isLoaded, setIsLoaded] = useState(false);

    const nameField = useRef();
    const [title, setTitle] = useState("");
    const [titleError, setTitleError] = useState("");

    const priceField = useRef();
    const [price, setPrice] = useState("");
    const [priceError, setPriceError] = useState("");

    const descriptionField = useRef();
    const [description, setDescription] = useState("");
    const [descriptionError, setDescriptionError] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        setIsLoaded(true);
    }, []);

    useEffect(() => {
        if (!isLoaded) return;
        priceField.current.focus();
    }, [isLoaded]);

    const onClickContinue = async () => {
        let hasErrors = false;

        if (!description) {
            setDescriptionError("Enter a description");
            descriptionField.current.focus();
            hasErrors = true;
        }


        if (!price) {
            setPriceError("Enter a price");
            priceField.current.focus();
            hasErrors = true;
        }

        if (price <= 0) {
            setPriceError("Price must be greater than zero");
            priceField.current.focus();
            hasErrors = true;
        }

        if (!title) {
            setTitleError("Enter a title");
            nameField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    return (
        <>
            <div className={styles.wrapper} >

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.title}>Edit product listing</div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="signUpName" className={styles.fieldLabel}>
                            Title
                        </label>
                        <input
                            ref={nameField}
                            id="signUpName"
                            className={`${styles.fieldInput} ${titleError && styles.errorInput}`}
                            type="text"
                            autoComplete="off"
                            value={title}
                            onChange={(e) => {
                                setTitleError("");
                                setTitle(e.target.value);
                            }}
                        />
                        {titleError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{titleError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="listingFormPrice" className={styles.fieldLabel}>
                            Price
                        </label>
                        <input
                            ref={priceField}
                            id="listingFormPrice"
                            className={`${styles.fieldInput} ${priceError && styles.errorInput}`}
                            type="number"
                            autoComplete="off"
                            value={price}
                            onChange={(e) => {
                                setPriceError("");
                                setPrice(e.target.value);
                            }}
                        />
                        {priceError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{priceError}</div>
                        </div>}
                    </div>

                    <div className={styles.fieldWrapper}>
                        <label htmlFor="listingFormDescription" className={styles.fieldLabel}>
                            Description
                        </label>
                        <textarea
                            ref={descriptionField}
                            id="listingFormDescription"
                            className={`${styles.fieldTextarea} ${descriptionError && styles.errorInput}`}
                            autoComplete="off"
                            value={description}
                            rows="10"
                            onChange={(e) => {
                                setDescriptionError("");
                                setDescription(e.target.value);
                            }}
                        />
                        {descriptionError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{descriptionError}</div>
                        </div>}
                    </div>

                    <button className={`${styles.continue} ${styles.noselect}`} onClick={onClickContinue}>Submit</button>
                </form>
            </div>
        </>
    );
}
