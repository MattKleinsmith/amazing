import { NavLink, useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./SignInForm.module.css";

export default function SignInForm() {
    const dispatch = useDispatch();

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                Form
            </div >
        </div>
    );
}
