import { adjectives, nouns } from "./words";
import nodemailer from "nodemailer";
import sgTransport from "nodemailer-sendgrid-transport";
import jwt from "jsonwebtoken";

export const generateSecret = () => {
  const randomNumber = Math.floor(Math.random() * adjectives.length);
  return `${adjectives[randomNumber]} ${nouns[randomNumber]}`;
};

const sendMail = async (email) => {
  const options = {
    auth: {
      api_user: process.env.SENDGRID_USERNAME,
      api_key: process.env.SENDGRID_PASSWORD,
    },
  };
  const client = nodemailer.createTransport(sgTransport(options));
  return client.sendMail(email);
};

export const sendSecretMail = (address, secret) => {
  const email = {
    from: "remember@rememberme.com",
    to: address,
    subject: "🌈  Login Secret from RememberMe",
    html: `🌟 Hello! <br> Your login secret is <strong>${secret}</strong><br>
    Please copy this and paste to login page.`,
  };

  return sendMail(email);
};

export const generateToken = (id) => {
  console.log(process.env.JWT_SECRET);
  return jwt.sign({ id }, process.env.JWT_SECRET);
};
