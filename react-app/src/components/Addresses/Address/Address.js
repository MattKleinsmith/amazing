import styles from "./Address.module.css";

import { useDispatch } from "react-redux";
import { NavLink } from 'react-router-dom';

import { deleteAddress } from "../../../store/addresses";

export default function Address({ address }) {
    const dispatch = useDispatch();
    const onClickDelete = () => {
        dispatch(deleteAddress(address.id));
    };

    return (
        <div className={styles.wrapper}>
            <div>{address.fullname}</div>
            <div>{address.address}</div>
            {address.building && <div>{address.building}</div>}
            <div>{address.city}</div>
            <div>{address.state}</div>
            <div>{address.zipcode}</div>
            <div>{address.region}</div>
            <div>{address.phone}</div>
            <NavLink to={`/addresses/${address.id}`}><button className={styles.button}>Edit</button></NavLink>
            <button onClick={onClickDelete} className={styles.button}>Remove</button>
            <button className={styles.button}>Set as Default</button>
        </div>
    );
}
