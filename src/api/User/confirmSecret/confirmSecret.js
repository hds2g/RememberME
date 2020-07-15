import { generateToken } from "../../../utils/utils";

export default {
  Mutation: {
    confirmSecret: async (_, args, { prisma }) => {
      const { email, secret } = args;
      try {
        const user = await prisma.user.findOne({ where: { email } });
        //console.log(user);
        if (user.loginSecret === secret) {
          return generateToken(user.id);
        } else {
          throw Error();
        }
      } catch (error) {
        console.log(error);
        throw Error("Wrong email/secret combination");
      }
    },
  },
};
