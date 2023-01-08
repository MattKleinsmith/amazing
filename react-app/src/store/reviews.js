import { csrfFetch } from './csrf';

const GET_REVIEWS = 'reviews/GET_REVIEWS';
const GET_REVIEW = 'reviews/GET_INDIVIDUAL_REVIEW';
const POST_REVIEW = 'reviews/POST_REVIEW';
const DELETE_REVIEW = 'reviews/DELETE_REVIEW';
const CLEAR_REVIEWS = 'reviews/CLEAR_REVIEWS';

export const getReviewsByProductId = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews`);
    const reviews = await response.json();
    dispatch({ type: GET_REVIEWS, reviews });
};

export const getReviewsByProductIdAndUser = (productId) => async dispatch => {
    const response = await csrfFetch(`/api/products/${productId}/reviews/current`);
    const review = await response.json();
    return review;
};

export const getReview = (reviewId) => async dispatch => {
    const response = await csrfFetch(`/api/reviews/${reviewId}`);
    const review = await response.json();
    return review;
};

export const postReview = body => async dispatch => {
    const response = await csrfFetch('/api/reviews', {
        method: "POST",
        body: JSON.stringify(body)
    });
    const review = await response.json();
    dispatch({ type: POST_REVIEW, review });
    return review.id;
};

export const putReview = (reviewId, body) => async dispatch => {
    await csrfFetch(`/api/reviews/${reviewId}`, {
        method: "PUT",
        body: JSON.stringify(body)
    });
    dispatch(getReview(reviewId));
};

export const postReviewImage = (reviewId, image) => async dispatch => {
    const formData = new FormData();

    formData.append('image', image);

    const response = await fetch(`/api/reviews/${reviewId}/images`, {
        method: "POST",
        body: formData
    });

    if (response.status >= 400) {
        const errors = await response.json();
        console.log(errors);
        throw errors;
    }
    dispatch(getReview(reviewId));
};

export const deleteReview = reviewId => async dispatch => {
    await csrfFetch(`/api/reviews/${reviewId}`, { method: "DELETE" });
    dispatch({ type: DELETE_REVIEW, reviewId });
};

export const deleteReviewImage = (reviewId, reviewImageId) => async dispatch => {
    await csrfFetch(`/api/review_images/${reviewImageId}`, { method: "DELETE" });
    dispatch(getReview(reviewId));
};

export const clearReviews = () => {
    return { type: CLEAR_REVIEWS };
}

export default function reviewsReducer(state = {}, action) {
    let newState = { ...state };
    switch (action.type) {
        case GET_REVIEWS:
            newState = {};
            for (const review of action.reviews) {
                newState[review.id] = review;
            }
            return newState;
        case POST_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case GET_REVIEW:
            newState[action.review.id] = action.review;
            return newState;
        case DELETE_REVIEW:
            delete newState[action.reviewId];
            return newState;
        case CLEAR_REVIEWS:
            return {};
        default:
            return state;
    }
};
