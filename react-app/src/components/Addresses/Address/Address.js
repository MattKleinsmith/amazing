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
            <div className={styles.name}>{address.fullname}</div>
            <div>{address.address.toUpperCase()}</div>
            {address.building && <div>{address.building.toUpperCase()}</div>}
            <div>{address.city.toUpperCase()}, {address.state.toUpperCase()} {address.zipcode.toUpperCase()}</div>
            <div>{address.region}</div>
            <div>Phone number: {address.phone}</div>
            <div className={styles.buttons}>
                <NavLink to={`/addresses/${address.id}`}>Edit</NavLink>
                <div> | </div>
                <div onClick={onClickDelete} className={styles.remove}>Remove</div>
            </div>
        </div>
    );
}
