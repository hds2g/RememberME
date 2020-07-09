import { generateSecret, sendSecretMail } from "../../../utils/utils";

export default {
  Mutation: {
    requestSecret: async (_, args, { prisma }) => {
      const { email } = args;

      const loginSecret = generateSecret();
      console.log("loginSecret: " + loginSecret);
      try {
        //await sendSecretMail(email, loginSecret);
        await prisma.user.update({
          data: { loginSecret },
          where: { email },
        });
        return true;
      } catch (error) {
        console.log(error);
        return false;
      }
    },
  },
};
