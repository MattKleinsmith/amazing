import { useDispatch } from 'react-redux';

import { setAddressModal } from '../../../store/ui';
import { Modal } from '../../../context/Modal';

import AddressForm from '../../AddressForm/AddressForm';

export default function AddressModal() {
    const dispatch = useDispatch();
    return <Modal onClose={() => dispatch(setAddressModal(false))}>
        <AddressForm isModal={true} />
    </Modal>;
}
