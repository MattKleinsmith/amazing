import styles from './ListingForm.module.css';

import { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams, useSearchParams } from 'react-router-dom';

import { postProduct, putProduct, postProductImage, deleteProductImage } from '../../store/products';
import { getProductDetails } from '../../store/productDetails';

export default function ListingForm() {
    const { productId } = useParams();
    const product = useSelector(state => state.productDetails)[productId];
    const source = useSearchParams()[0].get("source");
    const dispatch = useDispatch();

    const imageRef = useRef();
    const [image, setImage] = useState(null);
    const [imageError, setImageError] = useState("");

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
    }, [productId, product, dispatch]);

    useEffect(() => {
        setTitle(product?.title || "");
        setPrice(product?.price || 0);
        setDescription(product?.description || "");
    }, [product])

    useEffect(() => {
        titleField.current.focus();
    }, []);

    const handlePreviewChange = async (e) => {
        const file = e.target.files[0];
        if (!["image/png", "image/jpeg"].includes(file.type)) {
            setImageError("Please upload a png or jpeg image.");
            return;
        }
        setImage(file)
        const reader = new FileReader();
        reader.onload = function (e) {
            imageRef.current.src = e.target.result;
        }
        reader.readAsDataURL(file);

        if (productId && file) {
            await dispatch(postProductImage(productId, file, true, 1));
            dispatch(getProductDetails(productId));
        }
    }

    const onClickContinue = async () => {
        let hasErrors = false;

        if (description.trim().length < 10) {
            setDescriptionError("Please enter a description that's a least 10 characters long.");
            descriptionField.current.focus();
            hasErrors = true;
        }

        if (!price) {
            setPriceError("Please enter a price.");
            priceField.current.focus();
            hasErrors = true;
        }

        if (price <= 0 || price > 9999) {
            setPriceError("Price must be greater than zero and less than 10,000");
            priceField.current.focus();
            hasErrors = true;
        }

        if (!title) {
            setTitleError("Please enter a title.");
            titleField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;

        if (image || product?.preview_image) {
            try {
                const body = { title, price, description: description.trim() }
                const productThunkAction = product ? putProduct(productId, body) : postProduct(body);
                const newProductId = await dispatch(productThunkAction);
                try {
                    if (image && newProductId) {
                        await dispatch(postProductImage(newProductId, image, true, 1));
                    }
                }
                catch (responseBody) {
                    console.log(responseBody);
                }
            }
            catch (responseBody) {
                console.log(responseBody);
            }
            navigate(source ? source : "/inventory");
        }
        else {
            setImageError("Please upload a png or jpeg image for the product listing.");
        }
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    return (
        <>
            <div className={styles.wrapper}>

                <form className={styles.form} onSubmit={onSubmit}>
                    <div className={styles.heading}>{productId ? "Edit" : "Create"} product listing</div>
                    <div className={`${styles.fieldWrapper} ${styles.imageWrapper}`}>
                        {imageError && <div className={styles.imageError}>{imageError}</div>}
                        <img ref={imageRef} className={styles.image} src={product?.preview_image} alt={product?.preview_image} />
                        <label className={`${styles.fieldLabel} ${styles.imageLabel}`}>Search results image</label>
                        <input
                            type="file"
                            name="image"
                            accept="image/png, image/jpeg"
                            onChange={handlePreviewChange}
                            className={`${styles.imageInput}`}
                        />
                    </div>
                    <div className={styles.thumbnailListWrapper}>
                        {product?.images.map((image, i) => <img onClick={() => dispatch(deleteProductImage(product.id, image.id))} className={styles.thumbnail} src={image.url} key={i} alt={i} />)}
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

                    <button type="submit" className={`${styles.continue} ${styles.noselect}`}>{productId ? "Edit" : "Create"} listing</button>
                </form>
            </div>
        </>
    );
}
