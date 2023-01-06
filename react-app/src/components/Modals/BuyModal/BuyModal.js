import { useDispatch } from 'react-redux';

import { setBuyModal } from '../../../store/ui';
import { Modal } from '../../../context/Modal';
import BuyForm from './BuyForm';

export default function BuyModal() {
    const dispatch = useDispatch();
    return <Modal onClose={() => dispatch(setBuyModal(false))}>
        <BuyForm />
    </Modal>;
}
