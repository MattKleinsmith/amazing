import styles from "./Addresses.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from "react-router-dom";

import { getAddresses } from "../../store/addresses";

import Address from "./Address/Address";

export default function Addresses() {
    const addresses = useSelector(state => Object.values(state.addresses));
    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getAddresses());
    }, [dispatch]);
    return (
        <div className={styles.wrapper}>
            <div className={styles.bar}>
                <div className={styles.heading}>Your addresses</div>
                <div className={styles.addAddressWrapper}>
                    <NavLink to="/addresses/add"><button className={styles.addAddress}>Add Address</button></NavLink>
                </div>
            </div>
            <div className={styles.addresses}>
                {addresses.map((address, i) => <Address key={i} address={address} />)}
            </div>
        </div>
    );
}
