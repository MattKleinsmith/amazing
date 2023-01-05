import { useSelector } from 'react-redux';
import BuyModal from './BuyModal/BuyModal';

export default function Modals() {
    const ui = useSelector(state => state.ui);
    return <>
        {ui.buyModal?.showBuyModal && <BuyModal />}
    </>;
}
