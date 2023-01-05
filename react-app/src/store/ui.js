const SET_BUY_MODAL = 'ui/setBuyModal';

export const setBuyModal = (showBuyModal, productId, quantity) => { return { type: SET_BUY_MODAL, productId, showBuyModal, quantity }; };

export default function uiReducer(state = {}, action) {
    switch (action.type) {
        case SET_BUY_MODAL:
            return { ...state, buyModal: { showBuyModal: action.showBuyModal, quantity: action.quantity, productId: action.productId } };
        default:
            return state;
    }
};
