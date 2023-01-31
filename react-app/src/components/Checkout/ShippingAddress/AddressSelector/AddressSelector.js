import styles from "./AddressSelector.module.css";

import { useDispatch } from "react-redux";
import { setAddressModal } from "../../../../store/ui";
import { useNavigate } from "react-router";


export default function AddressSelector({ addressIdx, setAddressIdx, addresses }) {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const onEdit = () => {
        dispatch(setAddressModal(true));
        navigate(`?addressId=${addresses[addressIdx].id}`)
    };

    const onAdd = () => {
        dispatch(setAddressModal(true));
        navigate();
    };

    return <div className={styles.wrapper}>
        {addresses.map((address, i) => <div key={i} className={`${styles.content} ${i === addressIdx && styles.selected}`}>
            <input name="address" type="radio" id={`address_${i}`} readOnly defaultChecked={i === addressIdx} onClick={() => setAddressIdx(i)} />
            <label htmlFor={`address_${i}`} className={styles.address}>
                <span className={styles.bold}>{address.fullname} </span>
                <span>{address.address.toUpperCase()}, </span>
                <span>{address.city.toUpperCase()}, {address.state.toUpperCase()}, {address.zipcode.toUpperCase()}, {address.region.toUpperCase()} </span>
                <span className={styles.edit} onClick={onEdit}>Edit address</span>
            </label>
        </div>)}
        <div className={styles.row}>
            <img alt="add address" className={styles.addIcon} src="https://d1irxr40exwge2.cloudfront.net/addAddress.png" />
            <div className={`${styles.edit} ${styles.add}`} onClick={onAdd}>Add a new address</div>
        </div>
    </div>;
}
