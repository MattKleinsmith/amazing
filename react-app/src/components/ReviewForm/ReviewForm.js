import styles from './ReviewForm.module.css';

import { useState, useRef, useEffect, Fragment } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams, useSearchParams } from 'react-router-dom';

import { postReview, putReview, postReviewImage, getReviewsByProductIdAndUser, deleteReviewImage } from '../../store/reviews';
import { getProductDetails } from "../../store/productDetails";

export default function ReviewForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const { productId } = useParams();
    const source = useSearchParams()[0].get("source");

    const product = useSelector(state => state.productDetails)[productId];

    const [review, setReview] = useState(null);

    const titleField = useRef();
    const [title, setTitle] = useState(product?.title || "");
    const [titleError, setTitleError] = useState("");

    const [rating, setRating] = useState(review?.rating || 0);
    const [ratingError, setRatingError] = useState("");

    const imageRef = useRef();
    const [image, setImage] = useState(null);
    const [imageError, setImageError] = useState("");

    const reviewTextField = useRef();
    const [reviewText, setReviewText] = useState(review?.review || "");
    const [reviewTextError, setReviewTextError] = useState("");

    document.title = "Review Your Purchases";

    const emptyStar = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzgiIGhlaWdodD0iMzUiPjxkZWZzPjxwYXRoIGlkPSJhIiBkPSJNMTkgMGwtNS44NyAxMS41MkwwIDEzLjM3bDkuNSA4Ljk3TDcuMjYgMzUgMTkgMjkuMDIgMzAuNzUgMzVsLTIuMjQtMTIuNjYgOS41LTguOTctMTMuMTMtMS44NXoiLz48L2RlZnM+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48dXNlIGZpbGw9IiNGRkYiIHhsaW5rOmhyZWY9IiNhIi8+PHBhdGggc3Ryb2tlPSIjQTI2QTAwIiBzdHJva2Utb3BhY2l0eT0iLjc1IiBkPSJNMTkgMS4xbC01LjU0IDEwLjg4TDEuMSAxMy43Mmw4Ljk0IDguNDRMNy45MiAzNC4xIDE5IDI4LjQ2bDExLjA4IDUuNjQtMi4xMS0xMS45NCA4Ljk0LTguNDQtMTIuMzYtMS43NEwxOSAxLjF6Ii8+PC9nPjwvc3ZnPg==";
    const star = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzgiIGhlaWdodD0iMzUiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjUwJSIgeDI9IjUwJSIgeTE9IjI3LjY1JSIgeTI9IjEwMCUiPjxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiNGRkNFMDAiLz48c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNGRkE3MDAiLz48L2xpbmVhckdyYWRpZW50PjxwYXRoIGlkPSJiIiBkPSJNMTkgMGwtNS44NyAxMS41MkwwIDEzLjM3bDkuNSA4Ljk3TDcuMjYgMzUgMTkgMjkuMDIgMzAuNzUgMzVsLTIuMjQtMTIuNjYgOS41LTguOTctMTMuMTMtMS44NXoiLz48L2RlZnM+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48dXNlIGZpbGw9InVybCgjYSkiIHhsaW5rOmhyZWY9IiNiIi8+PHBhdGggc3Ryb2tlPSIjQTI2QTAwIiBzdHJva2Utb3BhY2l0eT0iLjc1IiBkPSJNMTkgMS4xbC01LjU0IDEwLjg4TDEuMSAxMy43Mmw4Ljk0IDguNDRMNy45MiAzNC4xIDE5IDI4LjQ2bDExLjA4IDUuNjQtMi4xMS0xMS45NCA4Ljk0LTguNDQtMTIuMzYtMS43NEwxOSAxLjF6Ii8+PC9nPjwvc3ZnPg=="

    useEffect(() => {
        async function fetchData() {
            if (productId && !product) {
                dispatch(getProductDetails(productId));
            }
            if (productId) {
                const _review = await dispatch(getReviewsByProductIdAndUser(productId)).catch(e => { });
                setReview(_review);
            }
        }
        fetchData();
    }, [productId, product, dispatch]);

    useEffect(() => {
        setTitle(review?.title || "");
        setRating(review?.rating || 0);
        setReviewText(review?.review || "");
    }, [review]);

    const appendImage = (url) => {
        console.log("appendImage", url);
        const img = document.createElement("img");
        img.src = url;
        img.className = styles.reviewImage;
        img.alt = "";
        imageRef.current.appendChild(img);

        const deleteWrapper = document.createElement("div");
        deleteWrapper.className = styles.deleteWrapper;
        deleteWrapper.onclick = () => {
            console.log("TODO: Delete image from array, and visually.");
        };
        imageRef.current.appendChild(deleteWrapper);

        const deleteImg = document.createElement("div");
        deleteImg.className = styles.delete;
        deleteWrapper.appendChild(deleteImg);
    }

    const handlePreviewChange = async (e) => {
        setImageError("");
        const file = e.target.files[0];
        if (!["image/png", "image/jpeg"].includes(file.type)) {
            setImageError("Please upload a png or jpeg image.");
            return;
        }
        setImage(file)

        if (review?.id && file) {
            await dispatch(postReviewImage(review.id, file));
            const _review = await dispatch(getReviewsByProductIdAndUser(productId)).catch(e => { });
            setReview(_review);
        } else {
            const reader = new FileReader();
            reader.onload = function (e) {
                appendImage(e.target.result);
            }
            reader.readAsDataURL(file);
        }
    }

    const onClickContinue = async () => {
        let hasErrors = false;

        if (!rating) {
            setRatingError("Please select a star rating");
            hasErrors = true;
        }

        if (rating < 1 || rating > 5) {
            setRatingError("Rating must be between 1 and 5");
            hasErrors = true;
        }

        if (!title) {
            setTitleError("Please enter your heading");
            titleField.current.focus();
            hasErrors = true;
        }

        if (!reviewText) {
            setReviewTextError("Please enter a written review");
            reviewTextField.current.focus();
            hasErrors = true;
        }

        if (hasErrors) return;

        try {
            const body = { title, rating, review: reviewText }
            const thunkAction = review ? putReview(review.id, body) : postReview(productId, body);
            const newReviewId = await dispatch(thunkAction);
            try {
                if (image && newReviewId) {
                    await dispatch(postReviewImage(newReviewId, image));
                }
            }
            catch (responseBody) {
                console.log(responseBody);
            }
        }
        catch (responseBody) {
            console.log(responseBody);
        }
        navigate(source ? source : `/listing/${productId}?source=reviews`);
    }

    const onSubmit = (e) => {
        e.preventDefault();
        onClickContinue();
    }

    const onImageDelete = async (reviewImageId) => {
        await dispatch(deleteReviewImage(reviewImageId));
        const _review = await dispatch(getReviewsByProductIdAndUser(productId)).catch(e => { });
        setReview(_review);
    }

    return (
        <>
            <div className={styles.wrapper}>

                <form className={styles.form} onSubmit={onSubmit}>

                    <div className={styles.heading}>{review ? "Edit" : "Create"} Review</div>

                    <div className={`${styles.fieldWrapper} ${styles.imageWrapper}`}>
                        <img className={styles.image} src={product?.preview_image} alt={product?.preview_image} />
                        <div className={styles.productTitle}>{product?.title}</div>
                    </div>

                    <div className={styles.line} />

                    <label htmlFor="listingFormTitle" className={styles.fieldLabel}>
                        Overall rating
                    </label>
                    <div className={styles.fieldWrapper}>
                        <img onClick={() => {
                            setRating(1);
                            setRatingError("");
                        }} alt="select to rate item one star" src={rating >= 1 ? star : emptyStar} />
                        <img onClick={() => {
                            setRating(2);
                            setRatingError("");
                        }} alt="select to rate item two star" src={rating >= 2 ? star : emptyStar} />
                        <img onClick={() => {
                            setRating(3);
                            setRatingError("");
                        }} alt="select to rate item three star" src={rating >= 3 ? star : emptyStar} />
                        <img onClick={() => {
                            setRating(4);
                            setRatingError("");
                        }} alt="select to rate item four star" src={rating >= 4 ? star : emptyStar} />
                        <img onClick={() => {
                            setRating(5);
                            setRatingError("");
                        }} alt="select to rate item five star" src={rating >= 5 ? star : emptyStar} />
                    </div>
                    {ratingError && <div className={styles.errorWrapper}>
                        <div className={styles.errorIcon} />
                        <div className={styles.errorText}>{ratingError}</div>
                    </div>}

                    <div className={styles.line} />

                    <label htmlFor="listingFormTitle" className={styles.fieldLabel}>
                        Add a headline
                    </label>
                    <div className={styles.fieldWrapper}>
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

                    <div className={styles.line} />

                    <label className={`${styles.fieldLabel} ${styles.imageLabel}`}>Add a photo</label>
                    <div className={styles.note}>Shoppers find images more helpful than text alone.</div>
                    <div className={styles.images}>
                        <div className={styles.images} ref={imageRef}>
                            {review && review.review_images.map((img, i) =>
                                <Fragment key={i}>
                                    <img src={img.url} alt="" className={styles.reviewImage} />
                                    <div onClick={() => onImageDelete(img.id)} className={styles.deleteWrapper} >
                                        <div className={styles.delete} />
                                    </div>
                                </Fragment>
                            )}
                        </div>
                        {review?.review_images.length < 4 && <label htmlFor="image" className={styles.addPhoto}>
                            <img alt="" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMjZweCIgaGVpZ2h0PSIyNnB4IiB2aWV3Qm94PSIwIDAgMjYgMjYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDUwLjIgKDU1MDQ3KSAtIGh0dHA6Ly93d3cuYm9oZW1pYW5jb2RpbmcuY29tL3NrZXRjaCAtLT4KICAgIDx0aXRsZT5TaGFwZTwvdGl0bGU+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxkZWZzPjwvZGVmcz4KICAgIDxnIGlkPSJzaHJpbmtJbWFnZUNUQS04MCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9ImV4cGwtY29weS0yMjkiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC00Ny4wMDAwMDAsIC0zMjMuMDAwMDAwKSIgZmlsbD0iI0FBQjdCOCIgZmlsbC1ydWxlPSJub256ZXJvIj4KICAgICAgICAgICAgPGcgaWQ9ImFzaW5NZXRhIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwgMTE5LjAwMDAwMCkiPgogICAgICAgICAgICAgICAgPGcgaWQ9ImFkZE1lZGlhIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjAwMDAwMCwgMTAwLjAwMDAwMCkiPgogICAgICAgICAgICAgICAgICAgIDxnIGlkPSJHcm91cCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTcuMDAwMDAwLCAxNy4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGcgaWQ9Ikdyb3VwLTIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLCA1Ny4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxwb2x5Z29uIGlkPSJTaGFwZSIgcG9pbnRzPSI0NC4zIDQxLjcgNDQuMyAzMCA0MS43IDMwIDQxLjcgNDEuNyAzMCA0MS43IDMwIDQ0LjMgNDEuNyA0NC4zIDQxLjcgNTYgNDQuMyA1NiA0NC4zIDQ0LjMgNTYgNDQuMyA1NiA0MS43Ij48L3BvbHlnb24+CiAgICAgICAgICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgICAgICAgICA8L2c+CiAgICAgICAgICAgICAgICA8L2c+CiAgICAgICAgICAgIDwvZz4KICAgICAgICA8L2c+CiAgICA8L2c+Cjwvc3ZnPg==" />
                        </label>}
                    </div>
                    {imageError && <div className={styles.imageError}>{imageError}</div>}
                    <input
                        type="file"
                        name="image"
                        id="image"
                        accept="image/png, image/jpeg"
                        onChange={handlePreviewChange}
                        className={`${styles.imageInput}`}
                        style={{ display: "none" }}
                    />

                    <div className={styles.line} />

                    <label htmlFor="listingFormDescription" className={styles.fieldLabel}>
                        Add a written review
                    </label>
                    <div className={styles.fieldWrapper}>
                        <textarea
                            ref={reviewTextField}
                            id="listingFormDescription"
                            className={`${styles.fieldTextarea} ${reviewTextError && styles.errorInput}`}
                            autoComplete="off"
                            value={reviewText}
                            rows="10"
                            onChange={(e) => {
                                setReviewTextError("");
                                setReviewText(e.target.value);
                            }}
                        />
                        {reviewTextError && <div className={styles.errorWrapper}>
                            <div className={styles.errorIcon} />
                            <div className={styles.errorText}>{reviewTextError}</div>
                        </div>}
                    </div>

                    <div className={styles.line} />

                    <button type="submit" className={`${styles.continue} ${styles.noselect}`}>{review ? "Edit" : "Create"} review</button>
                </form>
            </div>
        </>
    );
}
