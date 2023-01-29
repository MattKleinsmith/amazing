const SET_BUY_MODAL = 'ui/setBuyModal';
const SET_ADDRESS_MODAL = 'ui/setAddressModal';

export const setBuyModal = (showBuyModal, productId, quantity) => { return { type: SET_BUY_MODAL, productId, showBuyModal, quantity }; };
export const setAddressModal = (showAddressModal) => { return { type: SET_ADDRESS_MODAL, showAddressModal }; };

export default function uiReducer(state = {}, action) {
    switch (action.type) {
        case SET_BUY_MODAL:
            return { ...state, buyModal: { showBuyModal: action.showBuyModal, quantity: action.quantity, productId: action.productId } };
        case SET_ADDRESS_MODAL:
            return { ...state, addressModal: { showAddressModal: action.showAddressModal } };
        default:
            return state;
    }
};
