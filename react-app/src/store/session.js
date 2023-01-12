import { csrfFetch } from './csrf';
import { clearPurchases, getPurchases } from './purchases';
import { clearAddresses, getAddresses } from './addresses';

const SET_USER = 'session/setUser';

const setUser = user => {
    return { type: SET_USER, user }
};

export const restoreUser = () => async dispatch => {
    try {
        const response = await csrfFetch('/api/session');
        const user = await response.json();
        await dispatch(setUser(user))
        return response;
    } catch (errorResponse) {
    }
};

export const signIn = credentials => async dispatch => {
    // { email, password }
    const response = await csrfFetch('/api/session', {
        method: 'POST',
        body: JSON.stringify(credentials),
    });

    const user = await response.json();
    await dispatch(setUser(user));
    await dispatch(getAddresses());
    await dispatch(getPurchases());
    return user;
};

export const signOut = () => async (dispatch) => {
    await csrfFetch('/api/session', { method: 'DELETE', });
    await dispatch(setUser(null));
    await dispatch(clearAddresses());
    await dispatch(clearPurchases());
};

export const register = body => async (dispatch) => {
    const response = await csrfFetch("/api/users", {
        method: "POST",
        body: JSON.stringify(body)
    });
    const user = await response.json();
    dispatch(setUser(user));
};

export default function sessionReducer(state = { user: null }, action) {
    const newState = { ...state };
    switch (action.type) {
        case SET_USER:
            newState.user = action.user;
            return newState;
        default:
            return state;
    }
};
