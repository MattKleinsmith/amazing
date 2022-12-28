import styles from './ListingForm.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from 'react-router-dom';

import { postProduct, putProduct, postProductImage } from '../../store/products';
import { getProductDetails } from '../../store/productDetails';

export default function ListingForm() {
    const { productId } = useParams();
    const product = useSelector(state => state.productDetails)[productId];
    const dispatch = useDispatch();

    const [isLoaded, setIsLoaded] = useState(false);

    const previewImageRef = useRef();
    const [preview, setPreview] = useState(null);
    const [previewError, setPreviewError] = useState("");

    const titleField = useRef();
    const [title, setTitle] = useState(product?.title || "");
    const [titleError, setTitleError] = useState("");

    const priceField = useRef();
    const [price, setPrice] = useState(product?.price || 0);
    const [priceError, setPriceError] = useState("");

    const descriptionField = useRef();
    const [description, setDescription] = useState(product?.description || "");
    const [descriptionError, setDescriptionError] = useState("");

    const navigate = useNavigate();

    useEffect(() => {
        if (productId && !product) {
            dispatch(getProductDetails(productId));
        }
        setIsLoaded(true);
    }, [productId, product, dispatch]);

    useEffect(() => {
        if (!isLoaded) return;
        titleField.current.focus();
    }, [isLoaded]);

    const handlePreviewChange = (e) => {
        const file = e.target.files[0];
        setPreview(file)
        const reader = new FileReader();
        reader.onload = function (e) {
            previewImageRef.current.src = e.target.result;
        }
        reader.readAsDataURL(file);
    }

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
            titleField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;

        if (preview || product?.preview_image) {
            try {
                const body = { title, price, description }
                const productThunkAction = product ? putProduct(productId, body) : postProduct(body);
                const newProductId = await dispatch(productThunkAction);
                try {
                    if (preview) {
                        await dispatch(postProductImage(newProductId ? newProductId : productId, preview, true));
                    }
                }
                catch (responseBody) {
                    console.log(responseBody);
                }
            }
            catch (responseBody) {
                console.log(responseBody);
            }
            navigate("/inventory");
        }
        else {
            setPreviewError("Please upload an image for the product listing");
        }
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    return (
        <>
            <div className={styles.wrapper} >

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.heading}>{productId ? "Edit" : "Create"} product listing</div>
                    <div className={`${styles.fieldWrapper} ${styles.imageWrapper}`}>
                        {previewError && <div>{previewError}</div>}
                        <img ref={previewImageRef} className={styles.image} src={product?.preview_image} alt={product?.preview_image} />
                        <label className={`${styles.fieldLabel} ${styles.imageLabel}`}>Search results image</label>
                        <input
                            type="file"
                            name="image"
                            accept="image/png, image/jpeg"
                            onChange={handlePreviewChange}
                            className={`${styles.imageInput}`}
                        />
                    </div>
                    <div className={styles.fieldWrapper}>
                        <label htmlFor="listingFormTitle" className={styles.fieldLabel}>
                            Title
                        </label>
                        <input
                            ref={titleField}
                            id="listingFormTitle"
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
