import styles from './SignInForm.module.css';
import { useState } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../store/session";
import { NavLink } from 'react-router-dom';

export default function SignInForm() {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.signIn({ email, password }))
            .catch(e => {
                const errors = Object.entries(e.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
                setErrors(errors);
            });
    };

    const onClickContinue = () => {
        console.log("continue");
    }

    return (
        <div className={styles.wrapper} >
            <NavLink to="/" style={{ textDecoration: 'none' }}>
                <img src="/images/logo_black.png" alt="logo_black" />
            </NavLink>
            <form className={styles.signinForm} onSubmit={handleSubmit}>


                <div className={styles.signinHeader}>
                    <div className={styles.signIn}>Sign in</div>
                </div>
                {
                    errors.length > 0 && <ul className={styles.formErrors}>
                        {errors.map((error, idx) => <li key={idx}>{error}</li>)}
                    </ul>
                }
                <label >
                    Email <br />
                    <input
                        className="field"
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Password <br />
                    <input
                        className="field"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>

                <div className={styles.signindiv} onClick={onClickContinue}>Continue</div>

                <div type="submit" className={styles.demoButton} onClick={() => {
                    setEmail("demo@aa.io");
                    setPassword("password");
                }}>Log in as demo user</div>
            </form>
        </ div>

    );
}
