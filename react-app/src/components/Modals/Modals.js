import { useSelector } from 'react-redux';
import BuyModal from './BuyModal/BuyModal';
import AddressModal from './AddressModal/AddressModal';

export default function Modals() {
    const ui = useSelector(state => state.ui);
    return <>
        {ui.buyModal?.showBuyModal && <BuyModal />}
        {ui.addressModal?.showAddressModal && <AddressModal />}
    </>;
}
