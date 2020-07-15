import passport from "passport";
import { Strategy, ExtractJwt } from "passport-jwt";
const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();
//console.log(process.env.JWT_SECRET);

const jwtOptions = {
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
  secretOrKey: process.env.JWT_SECRET,
};

const verifyUser = async (payload, done) => {
  try {
    const user = await prisma.user.findOne({ where: { id: payload.id } });
    //console.log("verifyUser");
    //console.log(payload);
    // payload is one of JWT: header, payload, signature

    if (user !== null) {
      return done(null, user);
    } else {
      return done(null, false);
    }
  } catch (error) {
    return done(error, false);
  }
};

export const authenticateJwt = (req, res, next) => {
  //console.log(req);
  passport.authenticate("jwt", { sessions: false }, (error, user) => {
    if (user) {
      //console.log("authenticateJwt");
      req.user = user;
    }
    next();
  })(req, res, next);
};

passport.use(new Strategy(jwtOptions, verifyUser));
passport.initialize();
